import common_config



## dont modify
es_url = common_config.ES_HOST
es_header = common_config.HEADER


# config
url = "http://yyy"
param={
}

# run test
# get data from es
es_data = common_config.get_es_data("select aa from tableA")
aa = es_data[0]
es_data = common_config.get_es_data("select bb from tableB")
bb = es_data[0]
value = aa + bb

# get data from server

data_from_server = requests.post(url, param)
value_from_server = data_from_server['name']
# assert
if not value == value_from_server:
    # It is not a
    print('')




