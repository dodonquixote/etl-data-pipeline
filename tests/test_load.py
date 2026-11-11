import os
import pandas as pd
from utils.load import to_csv

def test_to_csv(tmp_path):
    df = pd.DataFrame([{"a": 1, "b": 2}])
    file = tmp_path / "test.csv"
    to_csv(df, str(file))
    df2 = pd.read_csv(file)
    assert df2.to_dict(orient="records") == [{"a": 1, "b": 2}]