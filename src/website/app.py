from flask import Flask, render_template, request, send_file
from src.scrapper.indeed_scrapper import IndeedScrapper
from src.csv.csv_writer import write_to_csv

app = Flask("Job Board")
job_data = []


# Render main page
@app.route('/')
def index():
    return render_template("index.html")


# Render search results page
@app.route('/search')
def search():
    global job_data
    keyword = request.args.get("keywords-field")
    print(keyword)
    location = request.args.get("location-field")
    indeed = IndeedScrapper(keyword, location)
    job_data = indeed.fetch_data()
    return render_template("search.html", count=len(job_data), keyword=keyword, location=location, data=job_data)


# Download csv
@app.route('/download')
def download():
    global job_data
    write_to_csv("job_data.csv", job_data)
    return send_file("job_data.csv")


if __name__ == '__main__':
    app.run(debug=True)
