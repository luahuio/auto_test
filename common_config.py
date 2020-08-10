
ES_HOST = "http://192.168.0.21:9200/_xpack/sql?format=json"

HEADER = {
        "X-Member-Id": "23832170000",
        "X-Region": "1100000",
        "X-Channel": "01",
        "Content-Type": "application/json;charset=UTF-8"
}

def get_es_data(sql):
        body = {"query": " %s " % (sql)}
        r = requests.post(url, headers=header, data=json.dumps(body))
        json_content = r.json()
        return json_content['rows']
