from flask import Flask, render_template, request
import requests
from bs4 import BeautifulSoup
import re

app = Flask(__name__)

def count_occurrences(url, search_text):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    text = soup.get_text()
    pattern = re.compile(search_text, re.IGNORECASE)
    matches = pattern.findall(text)
    return len(matches)

@app.route('/', methods=['GET', 'POST'])
def index():
    count = None
    if request.method == 'POST':
        url = request.form['url']
        search_text = request.form['search_text']
        count = count_occurrences(url, search_text)
    return render_template('index.html', count=count)

if __name__ == "__main__":
    app.run(debug=True)
