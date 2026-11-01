# Customer Segmentation & Marketing Analytics

**An interactive machine learning application for understanding customer purchasing behaviour and discovering actionable business insights.**

Built using Python, RFM analysis, K-Means clustering and Streamlit.

---

## Overview

Customer Segmentation & Marketing Analytics is a data analytics project that groups customers based on their purchasing behaviour.

The application uses **RFM analysis (Recency, Frequency and Monetary)** to create customer-level features and **K-Means clustering** to identify groups with similar purchasing patterns.

An interactive Streamlit dashboard presents customer segments, revenue contribution, purchasing patterns and suggested marketing strategies.

The project includes a synthetic transaction dataset for demonstration and supports uploading custom transaction CSV files.

## Dashboard Preview

### Customer Analytics

![Customer Analytics Dashboard](screenshots/Screenshot%202026-11-01%20152349.png)

*Customer KPIs, segment distribution, revenue contribution and overall analytics.*

### Customer Segment Analysis

![Customer Segment Analysis](screenshots/Screenshot%202026-11-01%20152400.png)

*Segment characteristics and customer purchasing frequency versus monetary value.*

### Marketing Recommendations & Customer Explorer

![Marketing Recommendations and Customer Explorer](screenshots/Screenshot%202026-11-01%20152412.png)

*Segment-specific marketing suggestions, customer filtering and downloadable reports.*

## Features

- Transaction data upload with CSV validation.
- Data cleaning and preprocessing.
- Customer-level RFM feature calculation.
- Log transformation and feature standardization.
- K-Means customer clustering.
- Silhouette score for cluster evaluation.
- Interactive customer segment visualizations.
- Segment-level revenue and spending analysis.
- Marketing recommendations based on customer profiles.
- Customer filtering and CSV report downloads.

## Technology Stack

| Area | Technologies |
|---|---|
| Programming | Python |
| Data Analysis | Pandas, NumPy |
| Machine Learning | Scikit-learn |
| Clustering Algorithm | K-Means |
| Analytics Technique | RFM Analysis |
| Data Preprocessing | Log Transformation, StandardScaler |
| Visualization | Plotly |
| Web Dashboard | Streamlit |
| Version Control | Git, GitHub |

## Methodology

The application follows this workflow:

1. **Data Collection:** Load transaction records from the sample dataset or an uploaded CSV.
2. **Data Cleaning:** Validate records and remove missing, duplicate and invalid transactions.
3. **RFM Analysis:** Calculate Recency, Frequency and Monetary values for each customer.
4. **Feature Engineering:** Apply log transformation and standardization to prepare the RFM features.
5. **Customer Clustering:** Apply K-Means to group customers according to purchasing behaviour.
6. **Evaluation:** Calculate silhouette score as a measure of cluster separation.
7. **Visualization:** Present segment characteristics, customer distribution and marketing recommendations.

## Customer Segments

The application assigns descriptive labels to clusters based on their relative RFM profiles.

| Segment | Interpretation | Suggested Action |
|---|---|---|
| Champions | Recent, frequent and high-spending customers | Reward and retain |
| Loyal / High Value | Customers with established purchasing activity | Strengthen loyalty |
| Potential Loyalists | Customers showing promising purchasing patterns | Encourage repeat purchases |
| Needs Attention | Customers with less recent or less frequent purchases | Re-engage carefully |

*Segment names are heuristic interpretations of cluster characteristics, not verified predictions of customer behaviour.*

## Project Structure

```text
customer-segmentation-project/
│
├── app.py
├── data/
│   └── sample_transactions.csv
│
├── src/
│   ├── __init__.py
│   └── pipeline.py
│
├── screenshots/
│   ├── Screenshot 2026-11-01 152349.png
│   ├── Screenshot 2026-11-01 152400.png
│   └── Screenshot 2026-11-01 152412.png
│
├── requirements.txt
├── .gitignore
└── README.md
```

## Installation and Execution

### Prerequisites

- Python 3.10 or newer
- pip

### 1. Clone the repository

```bash
git clone https://github.com/VarshaSV2005/customer-segmentation-project.git
```

### 2. Navigate to the project directory

```bash
cd customer-segmentation-project
```

### 3. Create and activate a virtual environment

**Windows:**

```bash
python -m venv .venv
.venv\Scripts\activate
```

**macOS / Linux:**

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Launch the application

```bash
streamlit run app.py
```

Open the local URL displayed in the terminal, usually:

`http://localhost:8501`

## Input Dataset

The application accepts transaction-level CSV data.

| Column | Description |
|---|---|
| `CustomerID` | Unique customer identifier |
| `InvoiceDate` | Transaction date |
| `Quantity` | Number of items purchased |
| `UnitPrice` | Price per item |
| `InvoiceNo` | Optional invoice identifier used for purchase frequency |

Each row represents an item on an invoice. If `InvoiceNo` is unavailable, each row is treated as a separate purchase.

The application uses synthetic sample data. When working with real business data, account for cancelled invoices, refunds, currencies and tax treatment.

## Evaluation and Limitations

- The silhouette score provides a clustering-quality diagnostic but does not independently establish business usefulness.
- The number of clusters should be evaluated using different K values and business interpretation.
- Recency is measured relative to the latest transaction date in the uploaded dataset.
- The application performs exploratory customer segmentation; it does not predict churn or future purchases.
- Marketing recommendations are suggestions based on segment profiles and require business validation.

## Future Enhancements

- Elbow method and automated K-value comparison.
- Customer Lifetime Value analysis.
- Customer cohort analysis.
- PostgreSQL database integration.
- FastAPI-based REST API.
- Model persistence and cloud deployment.
- Authentication and role-based access control.

## Author

**Varsha S V**

B.E. – Artificial Intelligence and Data Science

[GitHub Profile](https://github.com/VarshaSV2005)

---

<p align="center">
  <b>Customer Segmentation & Marketing Analytics</b><br/>
  Python · Machine Learning · Data Analytics
</p>
