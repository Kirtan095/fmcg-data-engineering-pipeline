import pandas as pd

def read_csv(path):
    """
    Reads a CSV file from given path and returns a DataFrame.
    Keeping this simple intentionally for learning purpose.
    """
    try:
        df = pd.read_csv(path)
        print(f"Loaded file: {path}")
        return df
    except Exception as e:
        print("Error reading file:", e)
        return None
