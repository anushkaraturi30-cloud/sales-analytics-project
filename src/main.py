from data_cleaning import load_and_clean_data
from analysis import calculate_kpis, revenue_by_region, monthly_sales
from visualization import (
    plot_revenue_by_region,
    plot_monthly_sales,
    plot_top_products,
)


def main():
    print("Program started...\n")

    # Load and clean data
    data = load_and_clean_data("../data/sales_data.csv")

    # Calculate KPIs
    kpis = calculate_kpis(data)

    print("===== BUSINESS SUMMARY =====")
    print(f"Total Revenue: ₹{kpis['total_revenue']}")
    print(f"Total Orders: {kpis['total_orders']}")
    print(f"Best Selling Product: {kpis['best_selling_product']}")
    print(f"Top Customer: {kpis['top_customer']}")

    print("\n===== Revenue by Region =====")
    print(revenue_by_region(data))

    print("\n===== Monthly Sales =====")
    print(monthly_sales(data))

    # Generate visualizations
    plot_revenue_by_region(revenue_by_region(data))
    plot_monthly_sales(monthly_sales(data))
    plot_top_products(data)

    print("\nCharts saved successfully in outputs/charts/")


if __name__ == "__main__":
    main()