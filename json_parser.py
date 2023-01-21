import os
import re
import json

directory = 'hackaton_2023_01/task_3/full_dataset/json/'

data = []

for n in range(10000):
    name = str(n) + '.json'
    try:
        with open(directory + name, "r") as readFile:
            jsonData = json.load(readFile)
            jsonData["id"] = n
            data.append(jsonData)
    except ValueError:
        continue

data

with open('merged_data.json', "w") as outfile:
    json.dump(data, outfile)
