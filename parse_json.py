import json
import os
from converttojson import find_file

file_array = []
appPath = os.getcwd() + "/output"
file_array_all = find_file('json')
for file_name in file_array_all:
    f = open(file_name, 'r')
    for line in f:
        y = json.loads(line)
        print(y['store_id'])
