import requests
from bs4 import BeautifulSoup
import jieba
from collections import Counter

#指定url
url = "https://nocturne-spider.baicizhan.com/practise/12.html"
headers = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36"}
#发送请求
response = requests.get(url,headers=headers)
html = response.text
soup = BeautifulSoup(html,'lxml')
content_all = soup.find_all(class_='short')
wordList = []
for content in content_all:
    contentString = content.string
    words = jieba.lcut(contentString)
    wordList = wordList + words
word_counts = Counter(wordList)
top_ten = word_counts.most_common(10)
print(top_ten)
