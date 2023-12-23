from flask import Flask, render_template, request
from src.scrapper.indeed_scrapper import IndeedScrapper

app = Flask("Job Board")

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/search')
def search():
    keyword = request.args.get("keywords-field")
    print(keyword)
    location = request.args.get("location-field")
    indeed = IndeedScrapper(keyword, location)
    job_data = indeed.fetch_data()
    return render_template("search.html", count=len(job_data), keyword=keyword, location=location, data=job_data)

if __name__ == '__main__':
    app.run(debug=True)
