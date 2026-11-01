# Customer Segmentation & Marketing Analytics

A beginner-friendly machine-learning portfolio project that groups customers using **RFM features** (Recency, Frequency, Monetary) and **K-Means clustering**, then presents the results in a Streamlit dashboard.

> The included CSV is synthetic demo data created for this project. It is not real customer data.

## Features

- Upload a transaction CSV or use the included demo data.
- Validate and clean transaction rows.
- Calculate customer-level RFM metrics.
- Apply log transformation, feature scaling, and K-Means clustering.
- Review a silhouette score as one clustering-quality diagnostic.
- Explore segment sizes, spend, revenue share, and customer records.
- View suggested marketing actions for each segment.
- Export customer-level and segment-summary CSV files.

## Requirements

- Python 3.10 or newer
- pip

## Run locally

### Windows (PowerShell)

```powershell
py -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
streamlit run app.py
```

If PowerShell blocks activation, run:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.venv\Scripts\Activate.ps1
```

### macOS / Linux

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install -r requirements.txt
streamlit run app.py
```

Streamlit will open the dashboard in your browser, usually at `http://localhost:8501`.

## Input CSV format

Each row should represent an item on an invoice. Required columns:

| Column | Meaning | Example |
|---|---|---|
| `CustomerID` | Customer identifier | `C0001` |
| `InvoiceDate` | Transaction date | `2025-10-10` |
| `Quantity` | Number of items | `2` |
| `UnitPrice` | Price per item | `19.99` |

Optional: `InvoiceNo` (used to count distinct purchases). If absent, each row is treated as a separate purchase.

The app excludes rows with missing required values, duplicate rows, non-positive quantities, and non-positive unit prices. Review your source data's cancelled invoices, refunds, currencies, and tax treatment before interpreting revenue.

## How it works

1. **Recency:** days since the customer's latest purchase, measured relative to the day after the latest transaction in the uploaded file.
2. **Frequency:** number of distinct invoices per customer.
3. **Monetary:** sum of quantity multiplied by unit price per customer.
4. **Preprocessing:** log1p transformation reduces skew; StandardScaler puts features on comparable scales.
5. **Clustering:** K-Means assigns customers to K groups.
6. **Interpretation:** segment names are assigned by relative cluster profiles. Names are heuristic descriptions, not guaranteed business truths.

## Important limitations

- This is exploratory segmentation, not a model that predicts future purchases or churn.
- The selected K value should be tested with several values and business interpretation; a silhouette score alone does not prove that clusters are useful.
- Recency is relative to the latest date in the uploaded dataset, not today's date.
- For real deployment, add privacy controls, access management, monitoring, currency normalization, returns handling, and data retention rules.
- Marketing actions should respect consent, opt-outs, and applicable privacy laws.

## Suggested next improvements

- Add an Elbow/Silhouette comparison for K=2..8.
- Add cohort and customer lifetime value analysis.
- Persist the trained scaler/model with joblib.
- Add database ingestion with PostgreSQL and an API with FastAPI.
- Add authentication and deployment.

## Repository structure

```text
customer-segmentation/
├── app.py
├── data/
│   └── sample_transactions.csv
├── src/
│   ├── __init__.py
│   └── pipeline.py
├── models/
├── reports/
├── requirements.txt
├── .gitignore
└── README.md
```

## Resume description

**Customer Segmentation & Marketing Analytics | Python, Pandas, Scikit-learn, Streamlit**
- Built an interactive customer analytics dashboard using RFM feature engineering and K-Means clustering.
- Cleaned transaction-level data, transformed and standardized features, and evaluated clusters using silhouette score.
- Presented customer segment profiles, revenue contribution, and segment-specific marketing recommendations.
