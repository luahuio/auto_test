#coding:utf-8
#连接本地es，使用sql语句查询并返回查询结果为json串
import requests
import json

def es_req_sql():
    url="http://192.168.0.21:9200/_xpack/sql?format=json"
    post_sql=input()
    body={"query": " %s " % (post_sql)}
    header={
        "X-Member-Id": "23832170000",
        "X-Region": "1100000",
        "X-Channel": "01",
        "Content-Type": "application/json;charset=UTF-8"
    }
    r=requests.post(url,headers=header,data=json.dumps(body))
    print(r.json())
if __name__ == "__main__":
    es_req_sql()

