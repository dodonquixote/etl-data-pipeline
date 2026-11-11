import requests
from bs4 import BeautifulSoup
from datetime import datetime

def scrape_all(pages=50):
    """Scrape product data from Fashion Studio site for given number of pages."""
    base_url = "https://fashion-studio.dicoding.dev/products?page={}"
    items = []
    for page in range(1, pages + 1):
        response = requests.get(base_url.format(page))
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        cards = soup.select('.product-card')
        for card in cards:
            title = card.select_one('.product-title').get_text(strip=True)
            price = card.select_one('.product-price').get_text(strip=True)
            rating = card.select_one('.product-rating').get_text(strip=True)
            colors = card.select_one('.product-colors').get_text(strip=True)
            size = card.select_one('.product-size').get_text(strip=True)
            gender = card.select_one('.product-gender').get_text(strip=True)
            timestamp = datetime.now().isoformat()
            items.append({
                'Title': title,
                'Price': price,
                'Rating': rating,
                'Colors': colors,
                'Size': size,
                'Gender': gender,
                'timestamp': timestamp
            })
    return items