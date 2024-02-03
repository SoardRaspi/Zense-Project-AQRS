import csv
import os
import requests
import json

import spacy
from spacy import displacy

curr_path = os.path.join(os.getcwd(), 'Maharashtra')
# file_target = 'content3_with_coords2.csv'

sno_new = 1
dic_list = []
# dictionary = {}

# with open(os.path.join(curr_path, file_target), 'a') as csvfile:
#     csvwriter = csv.writer(csvfile)
#     csvwriter.writerow(['sno', 'coords'])

with open(os.path.join(curr_path, 'content3.csv'), mode='r') as file:
    nlp = spacy.load('en_core_web_md')

    csvFile = csv.reader(file)
    csvFile = list(csvFile)

    for i in range(1, len(csvFile)):
    # for i in range(2, 3):
        try:
            sno, h, link, date = csvFile[i]
            h = h[1:len(h) - 1]
            h = h.split(',')

            for i in range(len(h)):
                h[i] = h[i].strip(" ")

            print(h)

            coords = []

            for H in h:
                doc = nlp(H)
                loc = ""

                count_dep = 0
                foi = False

                for token in doc:
                    if token.pos_ == 'ADP':
                        count_dep += 1

                    if (token.ent_type_ == 'FAC') or (token.ent_type_ == 'ORG') or (token.ent_type_ == 'GPE'):
                        foi = True

                    # print("token data:", token.text, "-", token.ent_type_, "-", token.lemma_)

                # if (count_dep <= 1) and (foi is True):
                if True:
                    loc = ' '.join(H.split()[1:])

                    q = "https://api.mapbox.com/geocoding/v5/mapbox.places/" + loc + ".json?access_token=sk.eyJ1Ijoic29hcmRyYXNwaSIsImEiOiJjbGw2ZDRvOW0wcG1vM2VsYTZkNTdqZHVkIn0.eAgcEEHmY7UZqdOf9TyJMw"
                    r = requests.get(q, headers=None).json()

                    # for feature in r['features']:
                    if 'features' in r:
                        feature = r['features'][0]
                        if 'Maharashtra' in feature['place_name']:
                            [long, lat] = feature['geometry']['coordinates']
                            coords.append([long, lat])

                    # print("loc:", loc, "data:", r)

            # print("coords_data:", coords)

            if len(coords) != 0:
                # with open(os.path.join(curr_path, file_target), 'a') as csvfile:
                #     csvwriter = csv.writer(csvfile)
                #     csvwriter.writerow([sno_new, coords])

                # dictionary[sno_new] = coords

                dictionary = {}

                dictionary["coords"] = coords
                dictionary["link"] = link
                dictionary["date"] = date

                print("dictionary:", dictionary)

                dic_list.append(dictionary)

                sno_new += 1

        except Exception as e:
            print("error:", e)

with open("coords_data3.json", "w") as outfile:
    json.dump(dic_list, outfile)