import requests
from bs4 import BeautifulSoup
url = "https://nocturne-spider.baicizhan.com/practise/8.html"
headers = {
    "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36"
}
response = requests.get(url, headers=headers)
html = response.text
soup = BeautifulSoup(html, "lxml")
content_all = soup.find_all(class_="TopicMovieIntro-awardItemTitle")
for content in content_all:
    contentString = content.text
    print(contentString)