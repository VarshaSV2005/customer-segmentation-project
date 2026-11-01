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

---

## About The Project

Customer Segmentation & Marketing Analytics is a data analytics and machine learning project that helps businesses understand their customers based on purchasing behaviour.

The project uses **RFM Analysis (Recency, Frequency, Monetary)** and **K-Means Clustering** to identify different customer groups.

It transforms raw transaction data into meaningful customer insights through an interactive Streamlit dashboard, helping businesses understand customer value, purchasing patterns and potential marketing opportunities.

## Dashboard Preview

### 1. Customer Analytics Dashboard

An overview of customer activity, business KPIs, segment distribution and revenue contribution.

![Customer Analytics Dashboard](<img width="1900" height="876" alt="Screenshot 2026-11-01 152349" src="https://github.com/user-attachments/assets/af4893d0-ab9c-4a04-a5df-3fa8b693ca26" />

)

### 2. Customer Segment Analysis

Explore customer characteristics and visualize the relationship between purchase frequency and customer spending.

![Customer Segment Analysis](<img width="1909" height="883" alt="Screenshot 2026-11-01 152400" src="https://github.com/user-attachments/assets/544e4d17-9a8c-4883-82ed-f0db3e24cf05" />
)

### 3. Marketing Recommendations & Customer Explorer

Explore marketing strategies for different customer groups, filter customer records and download analytical reports.

![Marketing Recommendations and Customer Explorer](<img width="1912" height="860" alt="Screenshot 2026-11-01 152412" src="https://github.com/user-attachments/assets/36b5d683-f28f-40b6-b70a-73ba19911c5d" />
)

---

## Key Features

- **Transaction Data Upload:** Upload custom customer transaction CSV files.
- **Data Preprocessing:** Validate and clean transaction records.
- **RFM Analysis:** Calculate Recency, Frequency and Monetary values for each customer.
- **K-Means Clustering:** Group customers according to their purchasing patterns.
- **Customer Segmentation:** Identify Champions, Loyal / High Value, Potential Loyalists and Needs Attention groups.
- **Interactive Dashboard:** Explore customer analytics through charts and visualizations.
- **Marketing Recommendations:** Generate suggested marketing actions for each segment.
- **Customer Explorer:** Filter and inspect individual customer records.
- **CSV Export:** Download customer lists and segment summaries.
- **Clustering Evaluation:** Use silhouette score to assess cluster separation.

## Technologies & Tools

| Category | Technologies |
|---|---|
| Programming Language | Python |
| Data Analysis | Pandas, NumPy |
| Machine Learning | Scikit-learn |
| Algorithm | K-Means Clustering |
| Analytics Method | RFM Analysis |
| Data Preprocessing | Feature Engineering, Log Transformation, StandardScaler |
| Visualization | Plotly |
| Dashboard | Streamlit |
| Development Tools | VS Code, Git, GitHub |

## How It Works

The project follows a six-step workflow:

**1. Data Collection**

Load the included sample transaction dataset or upload your own CSV file.

**2. Data Cleaning**

Validate transaction data and handle missing, duplicate and invalid records.

**3. RFM Feature Engineering**

Calculate three important customer metrics:

- **Recency:** How recently did the customer make a purchase?
- **Frequency:** How many distinct invoices did the customer generate?
- **Monetary:** How much money did the customer spend?

**4. Data Preprocessing**

Apply log transformation and StandardScaler to prepare customer features for clustering.

**5. Customer Clustering**

Apply the K-Means algorithm to group customers with similar purchasing behaviour. Use silhouette score to evaluate cluster separation.

**6. Business Insights**

Display customer segments, spending patterns, visualizations and suggested marketing strategies through the Streamlit dashboard.

## Understanding Customer Segments

| Segment | Description | Suggested Strategy |
|---|---|---|
| Champions | Recent, frequent and high-spending customers | Reward and retain |
| Loyal / High Value | Valuable customers with established purchase history | Strengthen loyalty |
| Potential Loyalists | Customers showing promising purchasing activity | Encourage repeat purchases |
| Needs Attention | Customers with less recent or less frequent purchases | Re-engage carefully |

*Segment labels are heuristic interpretations of cluster-level RFM characteristics. They are not manually verified customer classifications.*

## Project Structure

```text
customer-segmentation/
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
├── screenshots/
│   ├── dashboard-overview.png
│   ├── segment-analysis.png
│   └── customer-explorer.png
│
├── models/
├── reports/
│
├── requirements.txt
├── README.md
└── .gitignore
```

## Installation & Setup

### Step 1: Clone the repository

```bash
git clone https://github.com/YOUR-USERNAME/customer-segmentation.git
```

### Step 2: Navigate to the project

```bash
cd customer-segmentation
```

### Step 3: Create a virtual environment

```bash
python -m venv .venv
```

### Step 4: Activate the environment

**Windows:**

```bash
.venv\Scripts\activate
```

**macOS / Linux:**

```bash
source .venv/bin/activate
```

### Step 5: Install dependencies

```bash
pip install -r requirements.txt
```

### Step 6: Run the application

```bash
streamlit run app.py
```

Open the local URL displayed in your terminal:

```text
http://localhost:8501
```

## Input Dataset Format

Upload a CSV file containing the following required columns:

| Column | Description | Example |
|---|---|---|
| CustomerID | Unique customer identifier | C0001 |
| InvoiceDate | Transaction date | 2025-10-10 |
| Quantity | Number of items purchased | 2 |
| UnitPrice | Price per item | 19.99 |
| InvoiceNo | Invoice identifier | INV1001 |

Each row represents an item in a transaction. Refer to the application's expected CSV format for the exact input requirements.

## Learning Outcomes

- Practical experience with Python-based data analytics.
- Data cleaning and preprocessing using Pandas.
- Customer-level feature engineering using RFM analysis.
- Implementation of unsupervised machine learning.
- Applying K-Means clustering to customer transaction data.
- Evaluating clustering performance using silhouette score.
- Building interactive dashboards with Streamlit.
- Converting analytical results into business recommendations.

## Future Enhancements

- Customer Lifetime Value (CLV) analysis.
- Customer cohort analysis.
- Automated cluster optimization.
- Database integration for transaction management.
- REST API integration using FastAPI.
- Cloud deployment and authentication.

## Disclaimer

This project uses synthetic sample transaction data for demonstration and educational purposes. Customer segments and marketing recommendations are exploratory and should be validated against real business data before making business decisions.

---

<p align="center">
  <b>Built with Python, Machine Learning and a passion for Data Analytics.</b>
</p>

<p align="center">
  If you find this project interesting, feel free to explore the repository!
</p>
