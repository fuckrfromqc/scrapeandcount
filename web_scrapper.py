import requests
from bs4 import BeautifulSoup
import sys
import re

def count_occurrences(url, search_text):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    text = soup.get_text()
    pattern = re.compile(search_text, re.IGNORECASE)
    matches = pattern.findall(text)
    return len(matches)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python web_scraper.py [URL] [SEARCH_TEXT]")
        sys.exit(1)

    url = sys.argv[1]
    search_text = sys.argv[2]
    count = count_occurrences(url, search_text)
    print(f"The text '{search_text}' was found {count} times in the webpage '{url}'.")
