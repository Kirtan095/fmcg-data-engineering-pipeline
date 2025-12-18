import sqlite3
from read_data import read_csv
from clean_data import clean_sales_data, clean_master_data

DB_NAME = "fmcg_sales.db"


def load_table(df, table_name):
    """
    Loads a DataFrame into SQLite database.
    """
    conn = sqlite3.connect(DB_NAME)
    df.to_sql(table_name, conn, if_exists="replace", index=False)
    conn.close()
    print(f"Loaded table: {table_name}")


if __name__ == "__main__":


    # file paths
    products_path = "../data/raw_files/products.csv"
    stores_path = "../data/raw_files/stores.csv"
    sales_path = "../data/raw_files/sales_transactions.csv"

    # read data
    products_df = read_csv(products_path)
    stores_df = read_csv(stores_path)
    sales_df = read_csv(sales_path)

    # clean data
    products_df = clean_master_data(products_df)
    stores_df = clean_master_data(stores_df)
    sales_df = clean_sales_data(sales_df)

    # load to database
    load_table(products_df, "product_dim")
    load_table(stores_df, "store_dim")
    load_table(sales_df, "sales_fact")
