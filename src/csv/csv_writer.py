import os
import csv

HEADINGS = "TITLE, COMPANY, LOCATION, DESCRIPTION, URL\n"

def write_to_csv(filename, job_data):
    filename = f"{filename}"
    # Check if file exists, if not, add headings
    if not os.path.exists(filename):
        file = open(filename, "x")

    # overwrite data to the csv file
    with open(filename, "w", newline="") as file:
        file.write(HEADINGS)
        writer = csv.writer(file)
        for job in job_data:
            writer.writerow(job)
    file.close()

    print("Write to csv successful!")
