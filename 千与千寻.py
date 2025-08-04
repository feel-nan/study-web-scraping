import requests
from bs4 import BeautifulSoup
url = "https://nocturne-spider.baicizhan.com/2020/08/14/xun/"
response = requests.get(url)
html = response.text
soup = BeautifulSoup(html, "lxml")
content_all = soup.find_all("strong")
for content in content_all:
  contentString = content.string
  if contentString != None:
    print(contentString)