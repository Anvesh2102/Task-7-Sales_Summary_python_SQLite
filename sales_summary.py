import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

# ===== Create SQLite DB in memory =====
conn = sqlite3.connect(":memory:")   
cursor = conn.cursor()

# ===== Create sales table =====
cursor.execute("""
CREATE TABLE sales (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    product TEXT,
    quantity INTEGER,
    price REAL
)
""")

# ===== Insert sample data =====
sample_data = [
    ('Laptop', 5, 55000),
    ('Laptop', 3, 55000),
    ('Mobile', 10, 15000),
    ('Mobile', 7, 15000),
    ('Headphones', 15, 1200),
    ('Headphones', 20, 1200)
]

cursor.executemany("INSERT INTO sales (product, quantity, price) VALUES (?, ?, ?)", sample_data)
conn.commit()

# ===== Get full table to save =====
full_df = pd.read_sql_query("SELECT * FROM sales", conn)

# ===== SQL Summary Query =====
query = """
SELECT product,
       SUM(quantity) AS total_qty,
       SUM(quantity * price) AS revenue
FROM sales
GROUP BY product
"""

summary_df = pd.read_sql_query(query, conn)

# ===== Print results =====
print("\nSales Summary:\n")
print(summary_df)

# ===== Save files to disk =====
full_df.to_csv("sales_full_table.csv", index=False)
summary_df.to_csv("sales_summary.csv", index=False)

# ===== Plot bar chart =====
summary_df.plot(kind='bar', x='product', y='revenue')
plt.title("Revenue by Product")
plt.xlabel("Product")
plt.ylabel("Revenue")

# SAVE the chart to file
plt.savefig("sales_chart.png")
plt.show()

conn.close()
