"""
This file contains the code to scrap ZipRecruiter
"""
from zenrows import ZenRowsClient
from bs4 import BeautifulSoup

# Composing the URL
base_url = "https://www.ziprecruiter.com"
job_keywords = "Python Intern".replace(" ", "+")
location = "Mississauga"
URL = f"{base_url}/jobs-search?search={job_keywords}&location={location}"
print(URL)


# Getting the webpage using ZenRows
client = ZenRowsClient("b7c3e54a019e11ca18afb4a3d31038b9fb9cd46f")  # store in config
response = client.get(URL)
soup = BeautifulSoup(response.content, "html.parser")

job_elements = soup.find_all("div", {"class": "flex flex-col gap-24 md:gap-36"})

for job in job_elements:
    title_element = job.find("a", class_="break-words")  # get the title element with job title and link
    job_title = title_element.text  # remove prefix from job title
    job_url = base_url + title_element["href"]

    company_element = job.find("p", class_="line-clamp-1")
    company = company_element.text

    location_element = job.find("p", class_="text-body-md")
    location = location_element.text

    tag_element = job.find("div", {"class": "flex flex-col gap-4"})
    tags = tag_element.text

    print(job_title)
    print(company)
    print(location)
    print(tags)
    print(job_url)
    print()
