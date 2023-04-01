from flask import Flask, render_template, request
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

def count_occurrences(word, soup):
    text = soup.get_text().lower()
    words = text.split()
    return words.count(word.lower())

@app.route("/", methods=["GET", "POST"])
def index():
    count = None
    if request.method == "POST":
        url = request.form["url"]
        search_text = request.form["search_text"]
        response = requests.get(url)
        soup = BeautifulSoup(response.content, "html.parser")
        count = count_occurrences(search_text, soup)

    return render_template("index.html", count=count)

if __name__ == "__main__":
    app.run(debug=True)
