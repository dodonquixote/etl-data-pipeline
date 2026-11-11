import pytest
from unittest.mock import patch, Mock
from utils.extract import scrape_page

@patch("utils.extract.requests.get")
def test_scrape_page_success(mock_get):
    html = """
    <div class=\"product-card\">
      <span class=\"product-name\">Cool Jacket</span>
      <span class=\"product-price\">$99.99</span>
      <span class=\"product-colors\">3 Colors</span>
      <span class=\"product-size\">Size: M</span>
      <span class=\"product-gender\">Gender: Men</span>
    </div>
    """
    mock_resp = Mock()
    mock_resp.raise_for_status = Mock()
    mock_resp.text = html
    mock_get.return_value = mock_resp

    items = scrape_page("https://example.com")
    assert len(items) == 1
    p = items[0]
    assert p["title"] == "Cool Jacket"
    assert p["price"] == "$99.99"

@patch("utils.extract.requests.get")
def test_scrape_page_http_error(mock_get):
    mock_get.side_effect = Exception("Network error")
    with pytest.raises(Exception):
        scrape_page("https://bad-url")