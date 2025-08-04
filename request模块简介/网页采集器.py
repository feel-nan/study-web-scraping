# UA伪装：让爬虫对应的请求载体身份标识伪装成浏览器
import requests
if __name__ == "__main__":
  # UA伪装：将对应的User-Agent封装到一个字典中
  headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36 Edg/134.0.0.0'  
  }
  url = 'https://cn.bing.com/search'
  # 处理url携带的参数：封装到字典中
  kw = input('enter a word:')
  param = {
    'q':kw
  }
  # 对指定的url发起的请求对应的url是携带参数的，并且请求过程中处理了参数
  response = requests.get(url=url, params=param,headers=headers)
  page_text = response.text
  fileName =kw+ '.html'
  with open(fileName, 'w', encoding='utf-8') as fp:
    fp.write(page_text)
  print(fileName, '保存成功！！！')