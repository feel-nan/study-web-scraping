import requests
from bs4 import BeautifulSoup
url = "http://nocturne.bczcdn.com/zip/1625207762993_63705/web.html"
headers = {
    "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36"
}
response = requests.get(url, headers=headers)
# 手动设置编码为utf-8
response.encoding = 'utf-8' 
html = response.text
soup = BeautifulSoup(html, "lxml")
content_all = soup.find_all(class_="rank")
for content in content_all:
  title_list = content.find_all(name = "a")
  for title in title_list:
    titleString = title.string
    print(titleString)
