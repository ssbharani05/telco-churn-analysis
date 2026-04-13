# TelecomIQ — Customer Churn Analysis

End-to-end churn analytics project built with SQL, Python ML, and Tableau.

## Project Overview
- **Dataset:** 7,043 telecom customers
- **Churn Rate:** 26.54%
- **High Risk Customers:** 1,034
- **Model AUC:** 0.84 (84% accurate)

## Tech Stack
- **SQL** — MySQL data exploration and churn segmentation
- **Python** — EDA, Random Forest & Logistic Regression ML models
- **Tableau** — Interactive 5-page enterprise dashboard

## Live Dashboard
[View on Tableau Public](https://public.tableau.com/views/telco_churn_dashboard_17754770097670/Dashboard2)

## Project Structure
- `/sql` — MySQL churn analysis queries
- `/python` — ML model and EDA code
- `/tableau` — Tableau packaged workbook
- `/data` — Scored dataset with churn probabilities

## Key Findings
- Month-to-month contracts churn at 42.7% vs 2.8% for 2-year contracts
- Electronic check users churn at 3x the rate of credit card users
- New customers (0-12 months) churn at 47% — highest risk window
- Top churn drivers: Total Charges, Monthly Charges, Tenure
