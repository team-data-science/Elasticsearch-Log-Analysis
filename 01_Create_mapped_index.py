from elasticsearch import Elasticsearch
from numpy import source, take
import pandas as pd
from pandas import DataFrame
import json
import datetime as datetime



es = Elasticsearch("http://localhost:9200")

request_body = {
	    "settings" : {
	        "number_of_shards": 1,
	        "number_of_replicas": 1
	    },
	    'mappings': {
	            'properties': {
	                'process': {'type': 'text'},
	                'date': {'format': 'yyyy-MM-dd', 'type': 'date'},
	                'processing_time': {'type': 'double'},
	                'records': {'type': 'integer'},
					'run': {'type': 'integer'},
					'msg': {'type': 'text'}
	            }}
	}

print("creating 'example_index' index...")
es.indices.create(index = 'etl_monitoring', body = request_body)
