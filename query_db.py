import sqlite3
import pandas as pd

conn = sqlite3.connect("ecommerce.db")

query = """
SELECT 
    c.name AS customer_name,
    c.city,
    p.name AS product_name,
    p.category,
    o.order_date,
    oi.quantity,
    (p.price * oi.quantity) AS total_price
FROM orders o
JOIN customers c ON o.customer_id = c.customer_id
JOIN order_items oi ON o.order_id = oi.order_id
JOIN products p ON oi.product_id = p.product_id
ORDER BY total_price DESC
LIMIT 10;
"""

df = pd.read_sql_query(query, conn)
print("🧾 Top 10 Orders by Value:")
print(df)

conn.close()
