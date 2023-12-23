from src.scrapper.indeed_scrapper import IndeedScrapper
from src.csv.csv_writer import write_to_csv
import csv

def test_indeed():
    indeed = IndeedScrapper("Python Intern", "Toronto")
    job_data = indeed.fetch_data()
    assert job_data != []

def test_writing_csv():
    indeed = IndeedScrapper("Python Intern", "Toronto")
    job_data = indeed.fetch_data()
    write_to_csv("job_data.csv", job_data)

    with open("C:/Users/ariel/!Github/job-scrapper/src/csv/job_data.csv", "r") as file:
        reader = csv.reader(file)
        header = next(reader)
        assert next(reader) is not None

if __name__ == '__main__':
    import pytest
    pytest.main()
