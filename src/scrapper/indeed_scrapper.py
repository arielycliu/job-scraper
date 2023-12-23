"""
This file contains the code to scrap indeed
"""
from zenrows import ZenRowsClient
from bs4 import BeautifulSoup
import re

# Composing the URL
base_url = "https://ca.indeed.com"
job_keywords = "Intern"
location = "Mississauga"
page_count = 0  # starts at 0 for page 1 and increases by 10 each page
URL = f"{base_url}/jobs?q={job_keywords}&l={location}&start={page_count}"
print(URL)

# Getting the webpage using ZenRows
client = ZenRowsClient("b7c3e54a019e11ca18afb4a3d31038b9fb9cd46f")
response = client.get(URL)
soup = BeautifulSoup(response.content, "html.parser")

job_elements = soup.find_all("div", class_="job_seen_beacon")

for job in job_elements:
    title_element = job.find("a", class_="jcs-JobTitle")  # get the title element with job title and link
    title_pattern = re.compile(r'full details of ', re.IGNORECASE)  # set up regex pattern to match prefix
    job_title = re.sub(title_pattern, "", title_element['aria-label'])  # remove prefix from job title
    job_url = base_url + title_element["href"]

    company_element = job.find("span", {"data-testid": "company-name"})
    company = company_element.text

    location_element = job.find("div", {"data-testid": "text-location"})
    location = location_element.text

    tag_element = job.find("div", {"data-testid": "attribute_snippet_testid"})
    tags = tag_element.text

    snippet_element = job.find("div", class_="job-snippet").find("li")
    snippet = snippet_element.text

    print(job_title)
    print(company)
    print(location)
    print(tags)
    print(snippet)
    print(job_url)
    print()
