import requests
from bs4 import BeautifulSoup


url = "https://books.toscrape.com/"

response = requests.get(url)
soup = BeautifulSoup(response.text, "lxml")

print(soup.find("h3"))
