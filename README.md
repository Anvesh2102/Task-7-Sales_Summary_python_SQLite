# TASK 7 – Basic Sales Summary using SQLite & Python
## 📌 Objective

The goal of this task is to create a small SQLite database, run basic SQL queries using Python, and visualize the results through a simple bar chart. The task demonstrates:

1. Connecting Python to SQLite

2. Executing SQL queries for sales analysis

3. Displaying results using print statements

4. Generating a bar chart with Matplotlib

5. Exporting output to external files

## 🛠 Tools & Technologies Used
Tool	Purpose
Python	Programming environment
SQLite	Lightweight database system
Pandas	Data processing and SQL query loading
Matplotlib	Visualization
Visual Studio Code	Running code in local setup
📂 Dataset

## A temporary in-memory database (:memory:) is created with a sales table containing:

1. Product name

2. Quantity sold

3. Price

4. Sample records are inserted for testing.

## 🧠 Key SQL Query Used
SELECT product,
       SUM(quantity) AS total_qty,
       SUM(quantity * price) AS revenue
FROM sales
GROUP BY product;


## This query calculates:

1. Total units sold per product

2. Total revenue per product


## 📦 Generated Output Files
File	Description
sales_full_table.csv	Raw database records exported
sales_summary.csv	Summary of total quantity & revenue
sales_chart.png	Bar graph of revenue by product

## 🎯 Learning Outcomes

1. By completing this task, you will learn:

2. How to build and query a SQLite database

3. How to analyze data using Python & SQL

4. How to generate charts and export files

5. How to automate reporting workflows

