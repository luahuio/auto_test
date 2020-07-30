#coding:utf-8
import requests
import json

def req_by_config():
    js_path='/Users/hui/Downloads/config.json'
    with open(js_path,'r') as f:
        cases=json.loads(f.read())
        for key,value in cases.items():
            case_name=key
            case_config=value
            print("用例名称："+case_name)
            for key,value in case_config.items():
                config_name=key
                config=value
                if config_name == 'url':
                    url=config
                elif config_name == 'params':
                    params=config
                else:
                    headers=config
                    r=requests.get(url,params,headers=headers)
                    print(r.json())

if __name__=="__main__":
    req_by_config()