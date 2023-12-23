from src.scrapper.indeed_scrapper import IndeedScrapper
from csv_writer import write_to_csv

indeed = IndeedScrapper("Python Intern", "Toronto")
job_data = indeed.fetch_data()
print(job_data)
write_to_csv("job_data.csv", job_data)
