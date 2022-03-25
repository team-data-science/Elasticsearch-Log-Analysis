from elasticsearch import Elasticsearch
from numpy import source, take
import pandas as pd
from pandas import DataFrame
import json
import datetime as datetime


# initialize elasticsearch client
es = Elasticsearch("http://localhost:9200")

def index_first_run():
    # create logs for etl process run 1
    extract_json_1 = {
        'process': 'extract',
        'status' : 'success',
        'date': '2022-03-01',
        'processing_time': 5,
        'records': 5000,
        'run': 1
        }

    transform_json_1 = {
        'process': 'transform',
        'status' : 'success',
        'date': '2022-03-01',
        'processing_time': 5,
        'records': 5000,
        'run': 1
        }

    load_json_1 = {
        'process': 'load',
        'status' : 'success',
        'date': '2022-03-01',
        'processing_time': 5,
        'records': 5000,
        'run': 1
        }

    # write them to the index
    response = es.index(index = 'etl_monitoring',document = extract_json_1)
    response = es.index(index = 'etl_monitoring',document = transform_json_1)
    response = es.index(index = 'etl_monitoring',document = load_json_1)
    print(response)


# https://elasticsearch-py.readthedocs.io/en/latest/api.html?highlight=es.index#elasticsearch.Elasticsearch.index
# https://www.elastic.co/guide/en/elasticsearch/reference/7.16/docs-index_.html


# crate logs for etl run 2
def index_second_run():
    extract_json_2 = {
        'process': 'extract',
        'status' : 'success',
        'date': '2022-03-02',
        'processing_time': 10,
        'records': 10000,
        'run': 2
        }

    transform_json_2 = {
        'process': 'transform',
        'status' : 'success',
        'date': '2022-03-02',
        'processing_time': 10,
        'records': 10000,
        'run': 2
        }

    load_json_2 = {
        'process': 'load',
        'status' : 'success',
        'date': '2022-03-02',
        'processing_time': 10,
        'records': 9999,
        'run': 2
        }

    error_json_2 = {
        'process': 'load',
        'status' : 'error',
        'date': '2022-03-02',
        'processing_time': 5,
        'records': 1,
        'run': 1,
        'msg' : 'this is what happened'
        }

    # write them to the index
    response = es.index(index = 'etl_monitoring',document = extract_json_2)
    response = es.index(index = 'etl_monitoring',document = transform_json_2)
    response = es.index(index = 'etl_monitoring',document = load_json_2)
    response = es.index(index = 'etl_monitoring',document = error_json_2)
    print(response)

index_first_run()
index_second_run()

# write run 2 to the index
