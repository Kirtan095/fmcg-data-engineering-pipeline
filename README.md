# FMCG Sales Data Engineering Project

## About the Project
This project is a basic FMCG sales data engineering project that I created to
understand how raw business data is handled in a real-world scenario.

The main idea of this project is to take raw FMCG sales data from CSV files,
clean and process it using Python, store it in a database, and then analyze it
using SQL queries.

---

## Folder Structure
The project is organized in a simple and clear way:

data/
- raw_files/
  - products.csv
  - sales_transactions.csv
  - stores.csv

database/
- requirements.txt
- tables.sql

etl_scripts/
- read_data.py
- clean_data.py
- load_to_db.py

sql_queries/
- basic_analysis.sql

README.md

---

## Tools Used
- Python (Pandas, NumPy)
- SQLite for database
- SQL for analysis
- CSV files as data source
- VS Code

---

## How the Data Pipeline Works
1. First, raw sales data is read from CSV files.
2. Then the data is cleaned and processed using Python scripts.
3. After cleaning, the data is loaded into an SQLite database.
4. Finally, SQL queries are used to analyze sales performance.

This helped me understand the complete ETL flow in a simple way.

---

## Analysis Done
- Basic data cleaning
- Product-wise sales analysis
- Region-wise sales performance
- Simple SQL queries for insights

---

## Dataset Information
The dataset contains FMCG sales records such as:
- Product details
- Store and region information
- Quantity sold
- Sales revenue

---

## What I Learned
Through this project, I learned how data engineering pipelines work in practice.
I improved my skills in Python, SQL, handling structured data, and organizing
projects in a clean and readable format.

