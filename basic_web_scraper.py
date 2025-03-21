import requests
from bs4 import BeautifulSoup

def scrape_website(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        titles = soup.find_all('h2')  # Extracts all headings (h2 tags)
        
        print("Website Titles:")
        for idx, title in enumerate(titles, start=1):
            print(f"{idx}. {title.text.strip()}")
    else:
        print("Failed to fetch website data.")

# Example usage
website_url = "https://example.com"  # Replace with any website
scrape_website(website_url)
