#coding:utf-8
import requests #引用第三方库

def req_url():
    url="https://j.api.pupuvip.com/statistics/purchase_sale/overview"
    #传参，可以传无数个参数'key':'value'
    params={'time_date':'1596038400000','city_zip': '350100'}
    #请求头
    header={
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36',
        'authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjcwMTUiLCJqdGkiOiJjYzY3MjRlOS04ZGU2LTQ1YzEtYmRkMS02YTliNDJhYzViNjUiLCJnaXZlbl9uYW1lIjoi6LWW6L6J5ailIiwiR3JvdXAiOiIxZjg5NzNjNy0zZTMzLTRjZTgtYTg0NC04NzQ4Y2FhYzhlNzEiLCJUb2tlbiI6ImYxMmI4NDE5ZDNhOGI2MGY5YmE1OWFkMTA5MTcwZWQwYTcxYjFjOGMiLCJleHAiOjE1OTYyMDczODIsImlzcyI6Imh0dHA6Ly91Yy5wdXB1dmlwLmNvbSIsImF1ZCI6Imh0dHA6Ly91Yy5wdXB1dmlwLmNvbSJ9.keoPvtlqvJI0Z4JtOd2opkgGx0JKlKTT2bT7aVfn4Pk'
    }
    r=requests.get(url,params,headers=header)
    print(r.json())
if __name__ == "__main__":
    req_url()
