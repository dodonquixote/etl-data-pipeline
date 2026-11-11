import pandas as pd
from utils.extract import scrape_all
from utils.transform import transform
from utils.load import to_csv


def main():
    # Extract
    items = scrape_all(pages=50)
    df = pd.DataFrame(items)

    # Transform
    df_clean = transform(df)

    # Load to CSV
    to_csv(df_clean, "products.csv")

if __name__ == "__main__":
    main()