import glob
import json
import csv
import re
import time


start = time.time()
#import pandas as pd
from flatten_json import flatten

#Path of jsonl file
File_path = './input_data'
#reading all jsonl files
files = [f for f in glob.glob( File_path + "**/*.jsonl", recursive=True)]
i=0

#write header row
with open('./output_data/output.csv', 'a' , newline='') as g:
                writeheaders = csv.writer(g)
                writeheaders.writerow(['order_id','name','createdAt','processedAt','updatedAt'])
for f in files:
    with open(f, 'r') as F:
        for line in F:
#flatten json files 
            data = json.loads(line)
            data_1=flatten(data)
            normalize_id= re.search(r'\d+', data_1['id'])
            data_1['id'] = normalize_id[0]
#creating csv files  
            with open('./output_data/output.csv', 'a' , newline='') as f:
                thewriter = csv.writer(f)
#headers should be the Key values from json files that make Coulmn header
                thewriter.writerow([data_1['id'],data_1['name'],data_1['createdAt'],data_1['processedAt'],data_1['updatedAt']])
