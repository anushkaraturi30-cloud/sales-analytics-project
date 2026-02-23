import pandas as pd

def load_and_clean_data(file_path):
    # Load data
    df = pd.read_csv(file_path)

    # Convert date column
    df["date"] = pd.to_datetime(df["date"], errors="coerce")

    # Convert numeric columns
    df["quantity"] = pd.to_numeric(df["quantity"], errors="coerce")
    df["price"] = pd.to_numeric(df["price"], errors="coerce")

    # Remove missing values
    df = df.dropna()

    # Create total column
    df["total"] = df["quantity"] * df["price"]

    return df