import requests
from bs4 import BeautifulSoup
url = "https://nocturne-spider.baicizhan.com/practise/7.html"
headers = {
    "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36"
}
response = requests.get(url, headers=headers)
html = response.text
soup = BeautifulSoup(html, "lxml")
content_all = soup.find_all(class_="title")
for content in content_all:
    contentString = content.string
    if "怦然心动"== contentString:
        print("怦然心动是豆瓣top25电影")

    print(contentString)