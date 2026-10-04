# Exploratory Data Analysis

This notebook outline follows the Week 1 report.

## Questions

1. What is the overall on-time delivery rate?
2. Which traffic level has the highest average delay?
3. How does distance relate to actual delivery time?
4. Which vehicle type has the highest average delivery time?
5. Which delivery areas should receive additional operational attention?

## Suggested analysis

```python
import pandas as pd

df = pd.read_csv("../data/delivery_data.csv")

df["Delay_Minutes"] = (
    df["Actual_Delivery_Time"] - df["Planned_Delivery_Time"]
).clip(lower=0)

print(df.describe())
print(df.groupby("Traffic_Level")["Delay_Minutes"].mean())
print(df.groupby("Delivery_Area")["Delay_Minutes"].mean())
```

The dataset is simulated for demonstration and should not be described as real company data.
