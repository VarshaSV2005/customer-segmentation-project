# Customer Segmentation & Marketing Analytics

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10%2B-3776AB?style=for-the-badge&logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/Machine%20Learning-K--Means-orange?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Analysis-RFM-purple?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Dashboard-Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white" />
</p>

<p align="center">
  <b>Turning customer transaction data into actionable business insights using Python and Machine Learning.</b>
</p>

A beginner-friendly machine-learning portfolio project that groups customers using **RFM features** (Recency, Frequency, Monetary) and **K-Means clustering**, then presents the results in an interactive Streamlit dashboard.

> The included CSV is synthetic demo data created for this project. It is not real customer data.

---

## Dashboard Preview

### 1. Customer Analytics Dashboard

Explore customer activity, business KPIs, segment distribution and revenue contribution.

![Customer Analytics Dashboard](screenshots/Screenshot%202026-11-01%20152349.png)

### 2. Customer Segment Analysis

Understand customer segment characteristics and explore purchasing frequency against customer spending.

![Customer Segment Analysis](screenshots/Screenshot%202026-11-01%20152400.png)

### 3. Marketing Recommendations & Customer Explorer

Explore suggested marketing actions, filter customer records and download analytical reports.

![Marketing Recommendations and Customer Explorer](screenshots/Screenshot%202026-11-01%20152412.png)

---

## Features

- Upload a transaction CSV or use the included demo data.
- Validate and clean transaction rows.
- Calculate customer-level RFM metrics.
- Apply log transformation, feature scaling and K-Means clustering.
- Review a silhouette score as one clustering-quality diagnostic.
- Explore segment sizes, spending, revenue share and customer records.
- View suggested marketing actions for each segment.
- Export customer-level and segment-summary CSV files.

## Technologies Used

| Category | Technologies |
|---|---|
| Programming Language | Python |
| Data Analysis | Pandas, NumPy |
| Machine Learning | Scikit-learn |
| Algorithm | K-Means Clustering |
| Analytics Method | RFM Analysis |
| Data Preprocessing | Log Transformation, StandardScaler |
| Visualization | Plotly |
| Dashboard | Streamlit |
| Development Tools | VS Code, Git, GitHub |

## Requirements

- Python 3.10 or newer
- pip

## Run Locally

### 1. Clone the repository

```bash
git clone https://github.com/VarshaSV2005/customer-segmentation-project.git
```

### 2. Navigate to the project folder

```bash
cd customer-segmentation-project
```

### 3. Create a virtual environment

**Windows (PowerShell):**

```powershell
py -m venv .venv
.venv\Scripts\Activate.ps1
```

If PowerShell blocks activation, run:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.venv\Scripts\Activate.ps1
```

**macOS / Linux:**

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 4. Install dependencies

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

### 5. Run the application

```bash
streamlit run app.py
```

Streamlit will open the dashboard in your browser, usually at:

`http://localhost:8501`

## Input CSV Format

Each row should represent an item on an invoice.

| Column | Meaning | Example |
|---|---|---|
| `CustomerID` | Customer identifier | `C0001` |
| `InvoiceDate` | Transaction date | `2025-10-10` |
| `Quantity` | Number of items | `2` |
| `UnitPrice` | Price per item | `19.99` |

**Optional column:** `InvoiceNo`, used to count distinct purchases. If absent, each row is treated as a separate purchase.

The application excludes rows with missing required values, duplicate rows, non-positive quantities and non-positive unit prices.

Review your source data's cancelled invoices, refunds, currencies and tax treatment before interpreting revenue.

## How It Works

**1. Recency**

Measures the number of days since a customer's latest purchase, relative to the day after the latest transaction in the uploaded dataset.

**2. Frequency**

Counts the number of distinct invoices per customer.

**3. Monetary**

Calculates the total customer spending using quantity multiplied by unit price.

**4. Data Preprocessing**

Log transformation reduces feature skew, while StandardScaler brings features onto comparable scales.

**5. K-Means Clustering**

The algorithm groups customers into K clusters based on their purchasing behaviour.

**6. Customer Interpretation**

Cluster labels are assigned using relative cluster profiles. These are heuristic descriptions, not guaranteed business classifications.

## Important Limitations

- This is exploratory customer segmentation, not a model that predicts future purchases or customer churn.
- The selected K value should be tested across different values and interpreted in a business context.
- A silhouette score alone does not prove that clusters are useful.
- Recency is calculated relative to the latest transaction date in the uploaded dataset, not today's date.
- Real-world deployment requires privacy controls, access management, monitoring, currency normalization, returns handling and data-retention policies.
- Marketing actions should respect customer consent, opt-outs and applicable privacy laws.

## Future Improvements

- Add Elbow and Silhouette comparisons for K = 2 to 8.
- Add customer cohort and lifetime value analysis.
- Persist the trained scaler and model using Joblib.
- Integrate PostgreSQL for database management.
- Develop REST APIs using FastAPI.
- Add authentication and cloud deployment.

## Repository Structure

```text
customer-segmentation-project/
│
├── app.py
│
├── data/
│   └── sample_transactions.csv
│
├── src/
│   ├── __init__.py
│   └── pipeline.py
│
├── screenshots
