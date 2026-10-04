"""
Last-mile delivery analysis
Project: Strategic Planning and Data Exploration in Logistics

This project uses a simulated delivery dataset. Replace the CSV with approved
real data when available.
"""

from pathlib import Path
import pandas as pd

DATA_PATH = Path(__file__).resolve().parents[1] / "data" / "delivery_data.csv"


def load_data():
    data = pd.read_csv(DATA_PATH)
    data = data.drop_duplicates()
    return data


def add_features(data):
    data = data.copy()
    data["Delay_Minutes"] = (
        data["Actual_Delivery_Time"] - data["Planned_Delivery_Time"]
    ).clip(lower=0)
    return data


def calculate_kpis(data):
    on_time_rate = (data["Delivery_Status"].eq("On Time").mean() * 100)
    avg_delivery_time = data["Actual_Delivery_Time"].mean()
    cost_per_delivery = data["Delivery_Cost"].mean()

    # A failed delivery field is not present in the base dataset, so this
    # project uses delayed deliveries as an operational-risk indicator.
    delay_rate = data["Delivery_Status"].eq("Delayed").mean() * 100

    return {
        "on_time_delivery_rate_pct": round(on_time_rate, 2),
        "average_delivery_time_min": round(avg_delivery_time, 2),
        "average_cost_per_delivery": round(cost_per_delivery, 2),
        "delay_rate_pct": round(delay_rate, 2),
    }


def main():
    data = add_features(load_data())

    print("\n--- Dataset shape ---")
    print(data.shape)

    print("\n--- Missing values ---")
    print(data.isna().sum())

    print("\n--- KPI summary ---")
    for key, value in calculate_kpis(data).items():
        print(f"{key}: {value}")

    print("\n--- Delivery performance by traffic ---")
    print(
        data.groupby("Traffic_Level")["Delay_Minutes"]
        .agg(["count", "mean"])
        .round(2)
        .sort_values("mean", ascending=False)
    )

    print("\n--- Delivery performance by vehicle ---")
    print(
        data.groupby("Vehicle_Type")["Actual_Delivery_Time"]
        .mean()
        .round(2)
        .sort_values(ascending=False)
    )


if __name__ == "__main__":
    main()
