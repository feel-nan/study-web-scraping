import requests
from bs4 import BeautifulSoup
for num in range(1,10):
  url = f"https://ssr1.scrape.center/page/{num}"
response = requests.get(url)
html = response.text
soup = BeautifulSoup(html, "lxml")
content_all = soup.find_all(name="h2")
for content in content_all:
  contentString = content.string
  print(contentString)
