import os
import re
import json

directory = 'hackaton_2023_01/task_3/full_dataset/json/'
data = []
for n in range(10002):
    name = str(n) + '.json'
    try:
        with open(directory + name, "r") as readFile:
            jsonData = json.load(readFile)
        data.append(jsonData)
    except FileNotFoundError:
        continue

with open('merged_data.json', "w") as outfile:
    json.dump(data, outfile)

