import pandas as pd
from sqlalchemy import create_engine

class LoadError(Exception):
    """Custom exception for load failures"""
    pass


def to_csv(df: pd.DataFrame, path: str):
    try:
        df.to_csv(path, index=False)
    except Exception as e:
        raise LoadError(f"Failed to write CSV to {path}: {e}")


def to_gsheet(df: pd.DataFrame, spreadsheet_id: str, creds_file: str):
    # implement Google Sheets load using gspread + service account
    pass


def to_postgres(df: pd.DataFrame, conn_string: str, table_name: str = "products"):
    try:
        engine = create_engine(conn_string)
        df.to_sql(table_name, engine, if_exists="append", index=False)
    except Exception as e:
        raise LoadError(f"Failed to load to Postgres: {e}")