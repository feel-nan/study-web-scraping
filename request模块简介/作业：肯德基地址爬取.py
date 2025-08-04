import requests
import json
if __name__ == "__main__":
  url = "https://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=keyword"
  list_Dict = {
    'cname':'',
    'pid':'',
    'keyword':'徐州',
    'pageIndex':'1',
    'pageSize':'10',
  }
  headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36' 
  }
  response = requests.get(url=url,params=list_Dict,headers=headers)

  list_data = response.json()

  fp = open('./kfc.json','w',encoding='utf-8')

  json.dump(list_data,fp=fp,ensure_ascii=False)

  print("over!!!")