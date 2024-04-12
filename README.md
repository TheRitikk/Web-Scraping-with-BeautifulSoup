# Web-Scraping-with-BeautifulSoup
**main.py is a web scraping script written in Python using the requests, BeautifulSoup, json, re, and pandas libraries. It scrapes data from a list of URLs stored in an Excel file, extracts information such as title, text, image URLs, and links, and then saves the scraped data into a JSON file.**

Here's the breakdown of the code:

**Importing necessary libraries:**
<pre>
import requests
from bs4 import BeautifulSoup
import json
import re
import pandas as pd
	</pre>
**Defining the scrape_url function:**

This function takes a URL as input.
It sends a GET request to the URL and parses the HTML content using BeautifulSoup.
It extracts the title, text, image URLs, and links from the webpage.
Finally, it returns a dictionary containing the extracted data.


**Reading URLs from an Excel file:**
<pre>
df = pd.read_excel('urls.xlsx', header=None, names=['urls'])
urls = df['urls'].tolist()
	</pre>
**Scraping data from URLs:**

<pre>
scraped_data = [scrape_url(url) for url in urls if scrape_url(url)]
</pre>

This list comprehension iterates over each URL in the urls list, calls the scrape_url function for each URL, and appends the returned data (if not None) to the scraped_data list.

**Saving scraped data to a JSON file:**
<pre>
with open('scraped_data.json', 'w') as f:
    json.dump(scraped_data, f, indent=4)
  </pre>
This code block saves the scraped data into a JSON file named scraped_data.json. The json.dump() function is used to write the scraped_data list to the JSON file with an indentation of 4 spaces.

**Printing a completion message:**

<pre>
print("Scraping completed. Data saved in 'scraped_data.json'")
</pre>
This line prints a message indicating that the scraping process has been completed and the data has been saved to the JSON file.

This script provides a basic framework for web scraping from a list of URLs and storing the extracted data in a structured format for further analysis or processing.







