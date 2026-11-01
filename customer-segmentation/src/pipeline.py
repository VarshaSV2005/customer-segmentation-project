import numpy as np
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
from sklearn.preprocessing import StandardScaler

REQUIRED_COLUMNS = ["CustomerID", "InvoiceDate", "Quantity", "UnitPrice"]

def prepare_rfm(raw: pd.DataFrame):
    """Validate transaction data, clean basic errors, and aggregate to customer-level RFM."""
    df = raw.copy()
    missing = [c for c in REQUIRED_COLUMNS if c not in df.columns]
    if missing:
        raise ValueError("Missing required columns: " + ", ".join(missing))

    df["CustomerID"] = df["CustomerID"].astype("string").str.strip()
    df["InvoiceDate"] = pd.to_datetime(df["InvoiceDate"], errors="coerce")
    df["Quantity"] = pd.to_numeric(df["Quantity"], errors="coerce")
    df["UnitPrice"] = pd.to_numeric(df["UnitPrice"], errors="coerce")
    before = len(df)
    df = df.dropna(subset=REQUIRED_COLUMNS)
    df = df[(df["CustomerID"] != "") & (df["Quantity"] > 0) & (df["UnitPrice"] > 0)]
    df = df.drop_duplicates()
    warnings = []
    removed = before - len(df)
    if removed:
        warnings.append(f"Removed {removed:,} invalid, incomplete, duplicate, or non-positive transaction rows.")
    if df.empty:
        raise ValueError("No valid transaction rows remain after cleaning.")

    if "InvoiceNo" not in df.columns:
        df["InvoiceNo"] = df.index.astype(str)

    df["Revenue"] = df["Quantity"] * df["UnitPrice"]
    analysis_date = df["InvoiceDate"].max().normalize() + pd.Timedelta(days=1)
    rfm = df.groupby("CustomerID").agg(
        Recency=("InvoiceDate", lambda x: (analysis_date - x.max().normalize()).days),
        Frequency=("InvoiceNo", "nunique"),
        Monetary=("Revenue", "sum")
    )
    rfm = rfm[rfm["Monetary"] > 0].copy()
    if len(rfm) < 3:
        raise ValueError("At least 3 distinct customers are needed for clustering.")
    return rfm, df, warnings

def _label_segments(clustered: pd.DataFrame) -> pd.Series:
    """Assign readable labels based on relative RFM cluster profiles."""
    profiles = clustered.groupby("Cluster")[["Recency", "Frequency", "Monetary"]].mean()
    # Rank cluster profiles: more recent = lower recency; frequent/spending = higher.
    score = (
        profiles["Recency"].rank(ascending=True, pct=True) * 0.25
        + profiles["Frequency"].rank(ascending=True, pct=True) * 0.35
        + profiles["Monetary"].rank(ascending=True, pct=True) * 0.40
    )
    order = score.sort_values(ascending=False).index.tolist()
    labels = ["Champions", "Loyal / High Value", "Potential Loyalists", "Needs Attention",
              "At Risk", "New / Low History", "Hibernating", "Low Value"]
    mapping = {cluster: labels[i] for i, cluster in enumerate(order)}
    return clustered["Cluster"].map(mapping).rename("Segment")

def train_segments(rfm: pd.DataFrame, k: int = 4):
    features = rfm[["Recency", "Frequency", "Monetary"]].copy()
    # Log transform skewed transaction metrics, then standardize.
    transformed = np.log1p(features)
    scaler = StandardScaler()
    X = scaler.fit_transform(transformed)
    k = min(max(2, int(k)), len(rfm) - 1)
    model = KMeans(n_clusters=k, random_state=42, n_init=20)
    clusters = model.fit_predict(X)
    result = rfm.copy()
    result["Cluster"] = clusters
    result["Segment"] = _label_segments(result)
    sil = None
    if len(set(clusters)) > 1 and len(set(clusters)) < len(result):
        sil = float(silhouette_score(X, clusters))
    return result, {"silhouette": sil, "k": k, "inertia": float(model.inertia_)}

def segment_summary(segmented: pd.DataFrame) -> pd.DataFrame:
    total_revenue = segmented["Monetary"].sum()
    summary = segmented.groupby("Segment").agg(
        Customers=("Segment", "size"),
        **{
            "Avg Recency (days)": ("Recency", "mean"),
            "Avg Frequency": ("Frequency", "mean"),
            "Avg Monetary": ("Monetary", "mean"),
            "Revenue": ("Monetary", "sum")
        }
    ).reset_index()
    summary["Revenue Share (%)"] = np.where(total_revenue > 0, summary["Revenue"] / total_revenue * 100, 0)
    return summary.sort_values("Revenue", ascending=False)

def customer_recommendations(summary: pd.DataFrame) -> pd.DataFrame:
    actions = {
        "Champions": ("Reward and retain", "Offer early access, loyalty benefits, and referral incentives."),
        "Loyal / High Value": ("Grow loyalty", "Use personalized bundles and membership benefits; avoid unnecessary discounts."),
        "Potential Loyalists": ("Encourage repeat purchase", "Recommend relevant products and a modest second-purchase incentive."),
        "Needs Attention": ("Re-engage carefully", "Test a relevant reminder or limited offer and measure response."),
        "At Risk": ("Win-back campaign", "Send a targeted reminder or service check-in; suppress customers who opted out."),
        "New / Low History": ("Build the relationship", "Provide onboarding, product education, and a clear next-purchase path."),
        "Hibernating": ("Low-cost reactivation", "Try one low-cost reactivation message; stop if engagement remains low."),
        "Low Value": ("Serve efficiently", "Use low-cost channels and relevant recommendations rather than broad discounts.")
    }
    rows = []
    for segment in summary["Segment"]:
        action, reason = actions.get(segment, ("Test a segment-specific campaign", "Validate customer needs and test a small campaign."))
        rows.append({"Segment": segment, "Action": action, "Reason": reason})
    return pd.DataFrame(rows)
