"""
Simple baseline regression example.

The script predicts actual delivery time from numerical variables.
Categorical variables are converted with one-hot encoding.
"""

from pathlib import Path
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder
from sklearn.metrics import mean_absolute_error, r2_score

DATA_PATH = Path(__file__).resolve().parents[1] / "data" / "delivery_data.csv"


def main():
    df = pd.read_csv(DATA_PATH)

    X = df[
        [
            "Distance_km",
            "Shipment_Weight_kg",
            "Vehicle_Type",
            "Traffic_Level",
            "Weather",
        ]
    ]
    y = df["Actual_Delivery_Time"]

    categorical = ["Vehicle_Type", "Traffic_Level", "Weather"]
    numeric = ["Distance_km", "Shipment_Weight_kg"]

    preprocessor = ColumnTransformer(
        [
            ("categorical", OneHotEncoder(handle_unknown="ignore"), categorical),
            ("numeric", "passthrough", numeric),
        ]
    )

    model = Pipeline(
        [
            ("preprocessor", preprocessor),
            ("regressor", LinearRegression()),
        ]
    )

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.20, random_state=42
    )

    model.fit(X_train, y_train)
    predictions = model.predict(X_test)

    print("MAE:", round(mean_absolute_error(y_test, predictions), 2))
    print("R2:", round(r2_score(y_test, predictions), 3))


if __name__ == "__main__":
    main()
