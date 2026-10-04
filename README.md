# Last-Mile Delivery Optimization – Logistics Data Analyst Intern

A small Python project matching the Week 1 internship report:
**Strategic Planning and Data Exploration in Logistics**.

## Project objective

Analyze delivery operations and identify opportunities to improve:

- On-time delivery
- Delivery time
- Delivery cost
- Delay risk
- Vehicle/resource utilization

## Important note about the data

`data/delivery_data.csv` is a **simulated dataset created for this internship exercise**.
It is not presented as confidential company data or as real operational records.

## Repository structure

```text
logistics_last_mile_github_project/
├── data/
│   └── delivery_data.csv
├── notebooks/
│   └── 01_exploratory_analysis.md
├── src/
│   ├── analysis.py
│   ├── delivery_time_model.py
│   └── feature_engineering.py
├── .gitignore
├── README.md
└── requirements.txt
```

## Dataset fields

- `Order_ID`
- `Order_Date`
- `Delivery_Area`
- `Distance_km`
- `Shipment_Weight_kg`
- `Vehicle_Type`
- `Traffic_Level`
- `Weather`
- `Planned_Delivery_Time`
- `Actual_Delivery_Time`
- `Delivery_Status`
- `Delivery_Cost`
- `Customer_Rating`

## How to run

### 1. Create a virtual environment

```bash
python3 -m venv .venv
source .venv/bin/activate
```

On Windows:

```text
.venv\Scripts\activate
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Run KPI analysis

```bash
python src/analysis.py
```

### 4. Run the baseline delivery-time model

```bash
python src/delivery_time_model.py
```

## Methodology

The project follows:

**Data Collection → Data Cleaning → Exploratory Analysis → Feature Engineering → Predictive Modeling → Optimization → KPI Monitoring**

Regression is included as a baseline predictive method. Clustering and route optimization are proposed as future extensions.

## Connection to the internship report

The repository supports the report sections on:

- Logistics scenario
- KPIs
- Dataset design
- Data cleaning
- Exploratory analysis
- Regression
- Strategic roadmap
- Python implementation
- Expected outcomes

## Author

Sourav
