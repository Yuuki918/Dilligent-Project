import pandas as pd
import numpy as np
import os
from datetime import datetime, timedelta
import random

os.makedirs("data", exist_ok=True)

# Helper function to generate random dates
def random_date(start, end):
    delta = end - start
    return start + timedelta(days=random.randint(0, delta.days))

# 1️⃣ Customers
customers = pd.DataFrame({
    "customer_id": range(1, 21),
    "name": [f"Customer_{i}" for i in range(1, 21)],
    "email": [f"customer{i}@shop.com" for i in range(1, 21)],
    "city": np.random.choice(["Delhi", "Mumbai", "Bangalore", "Chennai", "Kolkata"], 20)
})
customers.to_csv("data/customers.csv", index=False)

# 2️⃣ Products
products = pd.DataFrame({
    "product_id": range(1, 11),
    "name": [f"Product_{i}" for i in range(1, 11)],
    "category": np.random.choice(["Electronics", "Clothing", "Home", "Books", "Sports"], 10),
    "price": np.random.randint(200, 3000, 10)
})
products.to_csv("data/products.csv", index=False)

# 3️⃣ Orders
start_date = datetime(2023, 1, 1)
end_date = datetime(2024, 12, 31)
orders = pd.DataFrame({
    "order_id": range(1, 51),
    "customer_id": np.random.choice(customers["customer_id"], 50),
    "order_date": [random_date(start_date, end_date).strftime("%Y-%m-%d") for _ in range(50)]
})
orders.to_csv("data/orders.csv", index=False)

# 4️⃣ Order Items
order_items = pd.DataFrame({
    "order_item_id": range(1, 101),
    "order_id": np.random.choice(orders["order_id"], 100),
    "product_id": np.random.choice(products["product_id"], 100),
    "quantity": np.random.randint(1, 5, 100)
})
order_items.to_csv("data/order_items.csv", index=False)

# 5️⃣ Reviews
reviews = pd.DataFrame({
    "review_id": range(1, 21),
    "product_id": np.random.choice(products["product_id"], 20),
    "rating": np.random.randint(1, 6, 20),
    "review_text": np.random.choice([
        "Good quality", "Excellent", "Worth the price", "Average", "Poor quality"
    ], 20)
})
reviews.to_csv("data/reviews.csv", index=False)

print("✅ Synthetic e-commerce CSV files generated in /data folder")
