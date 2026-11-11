import pytest
import pandas as pd
from utils.transform import clean_price, transform


def test_clean_price_valid():
    assert clean_price("$10.00") == 160000


def test_clean_price_unavailable():
    with pytest.raises(ValueError):
        clean_price("Price Unavailable")


def test_transform_dataframe():
    df = pd.DataFrame([
        {"title": "  Shirt  ", "price": "$5.00", "colors": "2 Colors", "size": "Size: L", "gender": "Gender: Women"}
    ])
    df_out = transform(df)
    assert df_out.iloc[0]["price"] == 80000
    assert df_out.iloc[0]["title"] == "Shirt"
    assert df_out.iloc[0]["colors"] == 2
    assert df_out.iloc[0]["size"] == "L"
    assert df_out.iloc[0]["gender"] == "Women"