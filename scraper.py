import requests
from bs4 import BeautifulSoup

url = "https://www.bbc.com/news"

response = requests.get(url)

print("Status Code:", response.status_code)

html_content = response.text

soup = BeautifulSoup(html_content, "html.parser")

headlines = soup.find_all("h2")

with open("headlines.txt", "w", encoding="utf-8") as file:
    for headline in headlines:
        title = headline.text.strip()

        if title:
            file.write(title + "\n")

print("Headlines saved successfully!")