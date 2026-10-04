import pandas as pd


def create_features(df: pd.DataFrame) -> pd.DataFrame:
    """Create analysis-ready features from the delivery dataset."""
    result = df.copy()

    result["Delay_Minutes"] = (
        result["Actual_Delivery_Time"] - result["Planned_Delivery_Time"]
    ).clip(lower=0)

    result["Distance_Band"] = pd.cut(
        result["Distance_km"],
        bins=[0, 5, 10, 20, float("inf")],
        labels=["Short", "Medium", "Long", "Very Long"],
        right=True,
    )

    return result
