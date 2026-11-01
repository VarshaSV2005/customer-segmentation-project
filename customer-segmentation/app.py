import streamlit as st
import pandas as pd
import plotly.express as px
from src.pipeline import prepare_rfm, train_segments, segment_summary, customer_recommendations

st.set_page_config(page_title="Customer Segmentation", page_icon="📊", layout="wide")
st.title("Customer Segmentation & Marketing Analytics")
st.caption("RFM analysis + K-Means clustering | Demo data is synthetic; upload your own transactions to analyze real customers.")

with st.sidebar:
    st.header("Data")
    use_sample = st.toggle("Use included sample data", value=True)
    uploaded = st.file_uploader("Or upload transaction CSV", type=["csv"])
    st.markdown("---")
    st.subheader("Clustering settings")
    k = st.slider("Number of customer groups (K)", min_value=2, max_value=8, value=4)
    st.caption("K is a starting choice. Compare silhouette scores and interpretability before using results for business decisions.")

if uploaded is not None:
    raw = pd.read_csv(uploaded)
elif use_sample:
    raw = pd.read_csv("data/sample_transactions.csv")
else:
    st.info("Turn on sample data or upload a CSV file to begin.")
    st.stop()

with st.expander("Expected CSV format"):
    st.write("Required columns: `CustomerID`, `InvoiceDate`, `Quantity`, `UnitPrice`. Optional: `InvoiceNo`.")
    st.write("Each row should represent an item on an invoice. Dates should be parseable. Cancelled invoices/returns should be excluded or reviewed before analysis.")

try:
    rfm, cleaned, warnings = prepare_rfm(raw)
    segmented, model_info = train_segments(rfm, k=k)
except Exception as exc:
    st.error(f"Could not process this file: {exc}")
    st.stop()

for warning in warnings:
    st.warning(warning)

summary = segment_summary(segmented)
total_customers = len(segmented)
total_revenue = float(cleaned["Revenue"].sum())
avg_spend = float(segmented["Monetary"].mean())

c1, c2, c3, c4 = st.columns(4)
c1.metric("Customers analyzed", f"{total_customers:,}")
c2.metric("Net sales in file", f"{total_revenue:,.2f}")
c3.metric("Average customer spend", f"{avg_spend:,.2f}")
c4.metric("Silhouette score", f"{model_info['silhouette']:.3f}" if model_info["silhouette"] is not None else "N/A")

st.subheader("Customer segment overview")
left, right = st.columns(2)
with left:
    fig = px.bar(summary, x="Segment", y="Customers", color="Segment", title="Customers by segment", text="Customers")
    st.plotly_chart(fig, use_container_width=True)
with right:
    fig = px.pie(summary, names="Segment", values="Customers", title="Segment share", hole=0.45)
    st.plotly_chart(fig, use_container_width=True)

st.subheader("Segment characteristics")
st.dataframe(summary.style.format({
    "Avg Recency (days)": "{:.1f}",
    "Avg Frequency": "{:.1f}",
    "Avg Monetary": "{:,.2f}",
    "Revenue Share (%)": "{:.1f}"
}), use_container_width=True, hide_index=True)

st.subheader("Customer map")
scatter = px.scatter(
    segmented.reset_index(), x="Frequency", y="Monetary", color="Segment",
    size="Monetary", hover_data=["CustomerID", "Recency"],
    title="Purchase frequency vs. customer spend"
)
st.plotly_chart(scatter, use_container_width=True)

st.subheader("Marketing recommendations")
recommendations = customer_recommendations(summary)
for _, row in recommendations.iterrows():
    with st.expander(f"{row['Segment']} — {row['Action']}"):
        st.write(row["Reason"])

st.subheader("Explore customers")
chosen = st.selectbox("Filter by segment", ["All"] + sorted(segmented["Segment"].unique().tolist()))
view = segmented.reset_index()
if chosen != "All":
    view = view[view["Segment"] == chosen]
st.dataframe(view, use_container_width=True, hide_index=True)

csv = view.to_csv(index=False).encode("utf-8")
st.download_button("Download displayed customer list (CSV)", csv, "customer_segments.csv", "text/csv")
summary_csv = summary.to_csv(index=False).encode("utf-8")
st.download_button("Download segment summary (CSV)", summary_csv, "segment_summary.csv", "text/csv")

st.caption("Important: This is an exploratory segmentation tool, not a validated prediction of future behaviour. Review data quality, cluster stability, and business context before acting on campaigns.")
