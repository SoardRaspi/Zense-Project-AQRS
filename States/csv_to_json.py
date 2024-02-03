import csv
import os
import json

curr_path = os.path.join(os.getcwd(), 'Maharashtra')
dictionary = {}

with open(os.path.join(curr_path, 'content3_with_coords2.csv'), mode='r') as file:
    csvFile = csv.reader(file)
    csvFile = list(csvFile)

    for i in range(1, len(csvFile)):
        pass

with open("coords_data2.json", "w") as outfile:
    json.dump(dictionary, outfile)