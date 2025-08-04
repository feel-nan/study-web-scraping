import requests
import json
if __name__ == "__main__":
  url = "https://movie.douban.com/j/chart/top_list"
  list_Dict = {
    'type':'24',
    'interval_id':'100:90',
    'action':'',
    # 从库中第几个开始取，取20个
    'start':'1',
    'limit':'1',
  }
  headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36' 
  }
  response = requests.get(url=url,params=list_Dict,headers=headers)

  list_data = response.json()

  fp = open('./douban.json','w',encoding='utf-8')

  json.dump(list_data,fp=fp,ensure_ascii=False)

  print("over!!!")
