import re
import pandas as pd
from datetime import datetime

class TransformError(Exception):
    """Custom exception for transform failures"""
    pass


def clean_price(price_str: str) -> int:
    """
    Convert '$12.345' → int(rupiah) with rate 1 USD = 16000 IDR.
    Raise ValueError for 'Price Unavailable' or bad format.
    """
    txt = price_str.strip()
    if txt.lower() == "price unavailable":
        raise ValueError("Price Unavailable")
    m = re.search(r"\$(\d[\d\.,]*)", txt)
    if not m:
        raise ValueError(f"Invalid price format: {txt}")
    # remove separators, parse float, convert
    usd = float(m.group(1).replace(".", ""))
    return int(usd * 16000)


def transform(df: pd.DataFrame) -> pd.DataFrame:
    """
    Clean and normalize scraped DataFrame:
     - clean price
     - strip prefixes
     - extract numeric colors
     - drop duplicates, nulls, invalid rows
     - add extraction timestamp
    """
    try:
        df["price"] = df["price"].apply(clean_price)
        df["title"]  = df["title"].str.strip()
        df["gender"] = df["gender"].str.replace(r"Gender:\\s*", "", regex=True).str.strip()
        df["colors"] = df["colors"].str.extract(r"(\d+)")[0].astype(int)
        df["size"]   = df["size"].str.replace(r"Size:\\s*", "", regex=True).str.strip()
        df["timestamp"] = datetime.utcnow()
        df = df.drop_duplicates().dropna()
        df = df[df["title"].str.lower() != "unknown product"]
        return df
    except Exception as e:
        raise TransformError(f"Failed to transform data: {e}")