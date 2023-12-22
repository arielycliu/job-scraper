"""
This file contains the code to scrape Glassdoor
"""

import requests
from bs4 import BeautifulSoup

URL = "https://www.glassdoor.ca/Job/mississauga-jobs-SRCH_IL.0,11_IC2280741.htm"
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
page = requests.get(URL, headers=headers)
print(page.text)

