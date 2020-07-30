#用在本地打开json，并进行解析
import json

js_path='/Users/hui/Downloads/huio.json'
with open(js_path,'r') as f:
    temp=json.loads(f.read())
#    data=temp['data']
#    for key,value in data.items():
 #       print(key,value)
    key1=temp['data']['gross_margin_fee_rate']