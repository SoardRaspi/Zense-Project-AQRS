import os
import json
import csv

f = open('coords_data2.json')

# returns JSON object as
# a dictionaryconv
data = json.load(f)

r = []

for d in data:
    for _ in d['coords']:
        r.append([float(_[0]), float(_[1])])

filename = "coords.csv"

with open(filename, 'w') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow([r])

# Iterating through the json
# # list
# for i in data:
#     print(i['coords'])