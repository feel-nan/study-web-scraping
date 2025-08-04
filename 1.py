# 使用import导入requests模块
import requests

# 将网页链接赋值给url
# url = "https://nocturne-spider.baicizhan.com/2020/07/29/example-post-3/"
url = "http://www.jsviat.edu.cn/"

# 使用requests.get()方法获取url的内容，将结果赋值给response
response = requests.get(url)

# 输出response
# print(response)
# 使用if语句判断.status_code属性获取的状态码等于200时
if response.status_code == 200:
    content = response.text[:1000]
    # 输出content
    print(content)
# 不满足条件时
else:
    # 输出：请求数据失败
    print("请求数据失败")
