"""
This file contains the code to scrap indeed
"""
from src.credentials import zenrows
from src.scrapper.exceptions import IndeedException
from zenrows import ZenRowsClient
from bs4 import BeautifulSoup
import re

class IndeedScrapper():
    def __init__(self, keywords, location):
        self.base_url = "https://ca.indeed.com"
        self.keywords = keywords
        self.location = location
        self.page_count = 0
        self.generate_url()

    def generate_url(self):
        self.url = f"{self.base_url}/jobs?q={self.keywords}&l={self.location}&start={self.page_count}"

    def fetch_data(self) -> list:
        try:
            # Getting the webpage using ZenRows
            client = ZenRowsClient(zenrows)
            response = client.get(self.url)
            soup = BeautifulSoup(response.content, "html.parser")

            # locate job divs, each containing a unique job
            job_elements = soup.find_all("div", class_="job_seen_beacon")

            job_entries = []

            for job in job_elements:
                title_element = job.find("a", class_="jcs-JobTitle")  # get the title element with job title and link
                title_pattern = re.compile(r'full details of ', re.IGNORECASE)  # set up regex pattern to match prefix
                # Extract Job title and URL from job heading
                job_title = re.sub(title_pattern, "", title_element['aria-label'])  # remove prefix from job title
                job_url = self.base_url + title_element["href"]
                # Extract company name
                company_element = job.find("span", {"data-testid": "company-name"})
                company = company_element.text
                # Extract location of job
                location_element = job.find("div", {"data-testid": "text-location"})
                location = location_element.text
                # Extract additional tags of the job
                tag_element = job.find("div", {"data-testid": "attribute_snippet_testid"})
                tags = tag_element.text
                # Extract the description of the job
                snippet_element = job.find("div", class_="job-snippet").find("li")
                snippet = snippet_element.text

                job_entry = [job_title, company, location, snippet, job_url]
                job_entries.append(job_entry)

            return job_entries
        except Exception as e:
            raise IndeedException()
