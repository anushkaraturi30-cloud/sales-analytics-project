import matplotlib.pyplot as plt
import os


def create_output_folder():
    """
    Creates outputs/charts folder if it does not exist.
    Returns the full path to the charts folder.
    """
    base_dir = os.path.dirname(os.path.dirname(__file__))
    output_path = os.path.join(base_dir, "outputs", "charts")
    os.makedirs(output_path, exist_ok=True)
    return output_path


def plot_revenue_by_region(region_data):
    """
    Generates and saves a bar chart of revenue by region.
    """
    output_path = create_output_folder()

    plt.figure(figsize=(8, 5))
    region_data.plot(kind="bar")

    plt.title("Revenue by Region")
    plt.xlabel("Region")
    plt.ylabel("Total Revenue")
    plt.xticks(rotation=45)
    plt.tight_layout()

    file_path = os.path.join(output_path, "revenue_by_region.png")
    plt.savefig(file_path)
    plt.close()


def plot_monthly_sales(monthly_data):
    """
    Generates and saves a line chart of monthly sales.
    """
    output_path = create_output_folder()

    plt.figure(figsize=(8, 5))
    monthly_data.plot(kind="line", marker="o")

    plt.title("Monthly Sales Trend")
    plt.xlabel("Month")
    plt.ylabel("Total Revenue")
    plt.xticks(rotation=45)
    plt.tight_layout()

    file_path = os.path.join(output_path, "monthly_sales.png")
    plt.savefig(file_path)
    plt.close()


def plot_top_products(df):
    """
    Generates and saves a bar chart of top 5 products by quantity sold.
    """
    output_path = create_output_folder()

    top_products = (
        df.groupby("product")["quantity"]
        .sum()
        .sort_values(ascending=False)
        .head(5)
    )

    plt.figure(figsize=(8, 5))
    top_products.plot(kind="bar")

    plt.title("Top 5 Products by Quantity Sold")
    plt.xlabel("Product")
    plt.ylabel("Total Quantity")
    plt.xticks(rotation=45)
    plt.tight_layout()

    file_path = os.path.join(output_path, "top_products.png")
    plt.savefig(file_path)
    plt.close()