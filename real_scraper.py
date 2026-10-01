import requests
from bs4 import BeautifulSoup

def real_propertypro_scrape():
    # Template for live scraping — activate when needed
    url = "https://www.propertypro.ng/for-rent/houses/abuja"
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'lxml')
    # Parse logic here...
    # For portfolio, we use mock to avoid getting blocked
    return []