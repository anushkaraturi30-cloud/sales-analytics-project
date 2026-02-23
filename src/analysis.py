import pandas as pd

def calculate_kpis(df):
    kpis = {}

    # Total revenue
    kpis["total_revenue"] = df["total"].sum()

    # Total orders
    kpis["total_orders"] = len(df)

    # Best selling product
    product_sales = df.groupby("product")["quantity"].sum()
    kpis["best_selling_product"] = product_sales.idxmax()

    # Top customer by revenue
    customer_sales = df.groupby("customer")["total"].sum()
    kpis["top_customer"] = customer_sales.idxmax()

    return kpis


def revenue_by_region(df):
    return df.groupby("region")["total"].sum().sort_values(ascending=False)


def monthly_sales(df):
    df["month"] = df["date"].dt.to_period("M")
    return df.groupby("month")["total"].sum().sort_index()