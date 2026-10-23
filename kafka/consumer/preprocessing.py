import pandas as pd
import math


def amount_bucket(amount):

    if amount < 50:
        return "Low"
    elif amount < 200:
        return "Medium"
    elif amount < 1000:
        return "High"
    else:
        return "Very High"


def safe_encode(value, encoder):

    if value in encoder.classes_:
        return encoder.transform([value])[0]

    return -1


def preprocess(transaction, encoders):

    df = pd.DataFrame([transaction])
    
    # Drop unwanted columns
    df.drop(
        columns=[
            "Unnamed: 0",
            "_c0",
            "first",
            "last",
            "street",
            "cc_num",
            "trans_num",
            "is_fraud"
        ],
        inplace=True,
        errors="ignore"
    )

    # Datetime conversion
    df["trans_date_trans_time"] = pd.to_datetime(df["trans_date_trans_time"])
    df["dob"] = pd.to_datetime(df["dob"])

    # Feature Engineering
    df["transaction_hour"] = df["trans_date_trans_time"].dt.hour

    df["day_of_week"] = (
        df["trans_date_trans_time"].dt.dayofweek + 1
    )

    df["transaction_month"] = (
        df["trans_date_trans_time"].dt.month
    )

    df["weekend_flag"] = (
        df["day_of_week"].isin([1, 7]).astype(int)
    )

    df["customer_age"] = (
        (pd.Timestamp.today() - df["dob"]).dt.days // 365
    )

    df["amount_bucket"] = (
        df["amt"].apply(amount_bucket)
    )

    df["merchant_distance"] = (
        (
            (df["lat"] - df["merch_lat"]) ** 2 +
            (df["long"] - df["merch_long"]) ** 2
        ) ** 0.5
    )

    # Label Encoding
    categorical_columns = [
        "merchant",
        "category",
        "gender",
        "city",
        "state",
        "job",
        "amount_bucket"
    ]

    for col in categorical_columns:
        df[col] = safe_encode(
            df[col].iloc[0],
            encoders[col]
        )

    # Drop unwanted columns
    drop_columns = [
        "trans_date_trans_time",
        "ingestion_timestamp",
        "source_system",
        "load_type",
        "dob"
    ]

    df.drop(
        columns=drop_columns,
        inplace=True,
        errors="ignore"
    )

    required_columns = [
        "merchant",
        "category",
        "amt",
        "gender",
        "city",
        "state",
        "zip",
        "lat",
        "long",
        "city_pop",
        "job",
        "unix_time",
        "merch_lat",
        "merch_long",
        "amount_bucket",
        "merchant_distance",
        "transaction_hour",
        "day_of_week",
        "transaction_month",
        "weekend_flag",
        "customer_age"
    ]

    df = df[required_columns]

    return df