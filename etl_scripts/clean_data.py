def clean_sales_data(df):
    """
    Basic cleaning for sales transactions.
    Intentionally kept simple for learning.
    """
    # remove duplicate rows
    df = df.drop_duplicates()

    # remove rows where important ids are missing
    df = df.dropna(subset=["product_id", "store_id"])

    return df


def clean_master_data(df):
    """
    Cleaning for product / store master data.
    """
    df = df.drop_duplicates()
    df = df.fillna("Unknown")
    return df
