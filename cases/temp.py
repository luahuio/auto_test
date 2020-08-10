import common_config
import os


def run_test(paramter):
    ## dont modify
    es_url = common_config.ES_HOST
    es_header = common_config.HEADER

    # config
    sever_url = "https://j.api.pupuvip.com/statistics/purchase_sale/overview"
    sever_param = paramter
    sever_header ={ "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36",
            "authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjcwMTUiLCJqdGkiOiJjYzY3MjRlOS04ZGU2LTQ1YzEtYmRkMS02YTliNDJhYzViNjUiLCJnaXZlbl9uYW1lIjoi6LWW6L6J5ailIiwiR3JvdXAiOiIxZjg5NzNjNy0zZTMzLTRjZTgtYTg0NC04NzQ4Y2FhYzhlNzEiLCJUb2tlbiI6ImYxMmI4NDE5ZDNhOGI2MGY5YmE1OWFkMTA5MTcwZWQwYTcxYjFjOGMiLCJleHAiOjE1OTYyMTEyNzksImlzcyI6Imh0dHA6Ly91Yy5wdXB1dmlwLmNvbSIsImF1ZCI6Imh0dHA6Ly91Yy5wdXB1dmlwLmNvbSJ9.p69nsfgbP8d62h7eMDH-Rwuw5oIHNrCXq-CScn3koJU"
        }

    # run test
    # get data from es
    es_data = common_config.get_es_data("select aa from tableA")
    aa = es_data[0]
    es_data = common_config.get_es_data("select bb from tableB")
    bb = es_data[0]
    value = aa + bb

    # get data from server
    data_from_server = requests.post(sever_url, sever_param)
    value_from_server = data_from_server['name']
    # assert
    if not value == value_from_server:
        # It is not a
        print('')


if __name__ == '__main__':
    paramters = [
        {
            time: 1
        },
        {
            city: 2
        }
    ]
    for (param : paramters.key):
        run_test(param)





