import requests
from bs4 import BeautifulSoup
import json
import re
import pandas as pd

def scrape_url(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for any HTTP error
        soup = BeautifulSoup(response.content, 'html.parser')

        if soup.title:
            title = soup.title.string
        else:
            title = "No title found"

        text = soup.get_text()
        pattern = re.compile(r'https?://\S+')
        links = [re.findall(pattern, str(soup))]

        
        img_tags = soup.find_all('img')
        img_urls = [img.get('src') for img in img_tags]
        
        # Store the scraped data in a dictionary
        data = {
            "url": url,
            "title": title,
            "image_urls": img_urls,
            "links": links,
            "text": text,
        }

        return data
    except Exception as e:
        return None


df = pd.read_excel('urls.xlsx', header=None, names=['urls'])

urls = df['urls'].tolist()

scraped_data = [scrape_url(url) for url in urls if scrape_url(url)]

with open('scraped_data.json', 'w') as f:
    json.dump(scraped_data, f, indent=4)

print("Scraping completed. Data saved in 'scraped_data.json'")
