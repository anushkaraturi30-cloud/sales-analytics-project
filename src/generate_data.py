import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random
import os

# Number of rows
n = 400

# Sample data
customers = ["Aditi", "Rahul", "Sneha", "Arjun", "Priya", "Rohan", "Kavya", "Vikas"]

products = {
    "Laptop": ("Electronics", 50000),
    "Phone": ("Electronics", 20000),
    "Tablet": ("Electronics", 15000),
    "Headphones": ("Accessories", 3000),
    "Monitor": ("Electronics", 12000),
    "Keyboard": ("Accessories", 1500)
}

regions = ["North", "South", "East", "West"]

# Date range
start_date = datetime(2024, 1, 1)

data = []

for i in range(n):
    product = random.choice(list(products.keys()))
    category, base_price = products[product]

    date = start_date + timedelta(days=random.randint(0, 365))
    customer = random.choice(customers)
    region = random.choice(regions)

    quantity = random.randint(1, 5)
    price = base_price + random.randint(-2000, 2000)

    data.append([
        date,
        customer,
        product,
        category,
        region,
        quantity,
        price
    ])

df = pd.DataFrame(data, columns=[
    "date", "customer", "product", "category", "region", "quantity", "price"
])

# Create correct path to data folder
base_dir = os.path.dirname(os.path.dirname(__file__))
data_path = os.path.join(base_dir, "data", "sales_data.csv")

os.makedirs(os.path.join(base_dir, "data"), exist_ok=True)

df.to_csv(data_path, index=False)

print("Dataset generated successfully!")