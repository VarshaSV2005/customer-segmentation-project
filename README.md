# Customer Segmentation & Marketing Analytics

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10%2B-3776AB?style=for-the-badge&logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/Machine%20Learning-K--Means-orange?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Analytics-RFM-purple?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Dashboard-Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white" />
</p>

<p align="center">
  <b>Transforming customer transaction data into meaningful business insights using Python and Machine Learning.</b>
</p>

A machine learning and data analytics project that identifies customer groups based on purchasing behaviour using **RFM Analysis (Recency, Frequency, Monetary)** and **K-Means Clustering**.

The project includes an interactive Streamlit dashboard that helps businesses understand customer value, discover purchasing patterns and explore targeted marketing opportunities.

> Demo dataset: The included transaction data is synthetic and created for demonstration purposes. It does not contain real customer information.

---

## Dashboard Preview

<p align="center">
  <img src="screenshots/project-preview.png" alt="Customer Segmentation and Marketing Analytics Dashboard" width="100%">
</p>

*Interactive dashboard preview featuring customer analytics, segment analysis, marketing recommendations and customer exploration.*

---

## Key Features

- **Transaction Data Upload:** Upload custom transaction CSV files or use the included sample dataset.
- **Data Cleaning:** Validate transaction records and remove invalid or duplicate rows.
- **RFM Analysis:** Calculate customer-level Recency, Frequency and Monetary values.
- **K-Means Clustering:** Group customers based on purchasing behaviour.
- **Customer Segmentation:** Identify Champions, Loyal / High Value, Potential Loyalists and Needs Attention groups.
- **Interactive Visualizations:** Explore customer distribution, revenue contribution and spending patterns.
- **Marketing Recommendations:** View suggested strategies for different customer segments.
- **Customer Explorer:** Filter and inspect individual customer records.
- **CSV Export:** Download customer-level and segment-summary reports.
- **Model Evaluation:** Review silhouette score as a clustering-quality diagnostic.

## Technologies Used

| Category | Technologies |
|---|---|
| Programming Language | Python |
| Data Analysis | Pandas, NumPy |
| Machine Learning | Scikit-learn |
| Algorithm | K-Means Clustering |
| Analytics | RFM Analysis |
| Data Preprocessing | Log Transformation, StandardScaler |
| Visualization | Plotly |
| Dashboard | Streamlit |
| Development Tools | VS Code, Git, GitHub |

## How It Works

The application follows a six-step workflow.

**1. Data Collection**

Load the included sample transaction dataset or upload your own CSV file.

**2. Data Cleaning**

Validate transaction records and handle missing values, duplicate rows and invalid transactions.

**3. RFM Feature Engineering**

Calculate three important customer metrics:

- **Recency:** How recently did the customer make a purchase?
- **Frequency:** How many distinct invoices did the customer generate?
- **Monetary:** How much money did the customer spend?

**4. Data Preprocessing**

Apply log transformation to reduce skew and StandardScaler to bring features onto comparable scales.

**5. Customer Clustering**

Use K-Means to group customers with similar purchasing patterns.

**6. Business Insights**

Explore customer groups, spending patterns, visualizations and suggested marketing actions through the Streamlit dashboard.

## Understanding Customer Segments

| Segment | Customer Behaviour | Suggested Strategy |
|---|---|---|
| Champions | Recent, frequent and high-spending customers | Reward and retain |
| Loyal / High Value | Valuable customers with established purchase history | Strengthen loyalty |
| Potential Loyalists | Customers showing promising purchasing activity | Encourage repeat purchases |
| Needs Attention | Customers with less recent or less frequent purchases | Re-engage carefully |

*Segment labels are heuristic interpretations of relative
