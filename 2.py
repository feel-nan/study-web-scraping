import requests
from bs4 import BeautifulSoup
url = "http://www.jsviat.edu.cn/"
response = requests.get(url)
html = response.text
soup = BeautifulSoup(html, "lxml")
content_all = soup.find_all("h1")
print( content_all)