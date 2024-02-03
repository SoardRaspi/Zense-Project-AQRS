import csv
import os
import json
import time

import spacy

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome('./chromedriver')
# driver2 = webdriver.Chrome('./chromedriver')

dict_list = []

curr_path = os.path.join(os.getcwd(), 'Maharashtra')

woi_arr = ['dead', 'injured', 'killed', 'wounded', 'missing', 'killing', 'injuries', 'injuring', 'injure', 'kill',
           'wound', 'injury', 'victims',

           'accident', 'crash', 'hit', 'smash', 'crush', 'collision', 'accidents', 'mishap', 'explosion', 'crashes',
           'crashed', 'collapsed', 'wreck', 'knocked']

roads = ["road", "highway", "expressway", "street", "lane", "avenue", "boulevard", "marg", "flyover", "walkover",
         "expy", "rd", "galli", "gali", "hwy", "rasta", "maarg", "path"]


def decimal_to_dms(decimal):
    degrees = int(decimal)
    minutes_float = (decimal - degrees) * 60
    minutes = int(minutes_float)
    seconds = int((minutes_float - minutes) * 60)
    return degrees, minutes, seconds


def lat_long_to_dms(latitude, longitude):
    lat_deg, lat_min, lat_sec = decimal_to_dms(abs(latitude))
    lat_dir = 'N' if latitude >= 0 else 'S'

    long_deg, long_min, long_sec = decimal_to_dms(abs(longitude))
    long_dir = 'E' if longitude >= 0 else 'W'

    # lat_dms = f"{lat_deg}° {lat_min}' {lat_sec}\" {lat_dir}"
    # long_dms = f"{long_deg}° {long_min}' {long_sec}\" {long_dir}"

    return [lat_deg, lat_min, lat_sec, lat_dir], [long_deg, long_min, long_sec, long_dir]

with open(os.path.join(curr_path, 'content3.csv'), mode='r') as file:
    nlp = spacy.load('en_core_web_md')

    csvFile = csv.reader(file)
    csvFile = list(csvFile)

    for i in range(1, len(csvFile)):
    # for i in range(3, 4):
        sno, content, link, date = csvFile[i]

        content_t = content[1:len(content) - 1]
        contents = content_t.split("',")

        soi = []

        for ii in range(len(contents)):
            curr_item = contents[ii].strip()

            if curr_item[0] == "'":
                curr_item = curr_item[1:]

            if curr_item[-1] == "'":
                curr_item = curr_item[:-1]

            contents[ii] = curr_item

        # print("contents:", contents)

        for item in contents:
            soi.append(item)

            words = item.split()

            flag_done = False
            for related in woi_arr:
                if flag_done is False:
                # if True:
                    if nlp(words[0]).similarity(nlp(related)) > 0.7:
                    # if True:
                        soi.append(item)
                        flag_done = True

        print("sno:", sno, "soi:", soi)

        if len(soi) != 0:
        # if True:
            coords = []

            for sentence in soi:
                # print(sentence)

                driver.get(
                    "https://developers-dot-devsite-v2-prod.appspot.com/maps/documentation/utils/geocoder#q%3D" +
                    str(sentence))

                # articles = driver.find_elements(By.CLASS_NAME, "result-formatted-address")[0]
                # articles = driver.find_elements(By.XPATH, '//*[@id="result-0"]/table/tbody/tr/td[2]/p[2]')

                time.sleep(5)
                articles = driver.find_elements(By.XPATH, '//div[@id="results-control-ui"]')

                for article in articles:
                    try:
                        # articles = driver.find_elements(By.XPATH, '//p[@class="result-formatted-address"]')[0]

                        if ' no results (ZERO_RESULTS)' not in article.text:
                            article_sentences = article.text.split('\n')

                            flag_road = False

                            for word_road in sentence.split(" "):
                                if flag_road is False:
                                    if word_road.lower() in roads:
                                        flag_road = True

                            # print(sentence, ":", flag_road)

                            if True:
                                flag_address = False

                                for article_sentence in article_sentences:
                                    if flag_address is False:
                                        if ('Address' in article_sentence) and ('Maharashtra' in article_sentence):
                                            flag_address = article_sentences.index(article_sentence)

                                # if flag_address is not False:
                                if True:
                                    coordinates_sentence = article_sentences[flag_address + 1]
                                    # print("coordinates_sentence:", coordinates_sentence)

                                    end_index = coordinates_sentence.index(' (type: ')
                                    mid_index = coordinates_sentence.index(',')

                                    lat = coordinates_sentence[10:mid_index]
                                    long = coordinates_sentence[mid_index + 1:end_index]

                                    if flag_road is True:
                                        try:
                                            # lat_dms, long_dms = lat_long_to_dms(float(lat), float(long))
                                            #
                                            # driver2.get(f"https://www.google.com/maps/place/"
                                            #             f"{lat_dms[0]}%C2%B0{lat_dms[1]}'{lat_dms[2]}%22{lat_dms[3]}+"
                                            #             f"{long_dms[0]}%C2%B0{long_dms[1]}'{long_dms[2]}%22{long_dms[3]}/@"
                                            #             f"{lat},{long}")
                                            #
                                            # time.sleep(2)
                                            #
                                            # address_road = driver2.find_elements(By.XPATH, '//span[@class="DkEaL"]')[0].text
                                            # print("address_road:", address_road)

                                            # print("address_road:", address_road.get_property("innerText"))

                                            # driver2.get(
                                            #     "https://developers-dot-devsite-v2-prod.appspot.com/maps/documentation/utils/geocoder#q%3D" +
                                            # coordinates_sentence[10:mid_index] + ", " + coordinates_sentence[mid_index + 1:end_index])
                                            #
                                            # time.sleep(5)
                                            # article_i = driver2.find_elements(By.XPATH, '//div[@id="results-control-ui"]')[0]
                                            #
                                            # article_sentences_i = article_i.text.split('\n')
                                            #
                                            # flag_address_i = False
                                            #
                                            # for article_sentence_i in article_sentences_i:
                                            #     if flag_address_i is False:
                                            #         if ('Address' in article_sentence_i) and ('Maharashtra' in article_sentence_i):
                                            #             flag_address_i = True
                                            #
                                            #             article_rd = article_sentence[article_sentence_i.index(',') + 1:]
                                            #             article_rd = article_rd[:article_rd.index(',')]
                                            #             article_rd.strip()
                                            #
                                            #             print("inner:", [article_sentence_i[:article_sentence_i.index(',')].strip(),
                                            #                            article_rd])
                                            #

                                            # flag_address_road = False
                                            # address_road_t = address_road.split(",")
                                            # for ___ in range(len(address_road_t)):
                                            #     address_road_t[___] = address_road_t[___].strip().lower()
                                            #
                                            #     for word_road in address_road_t[___].split():
                                            #         if flag_address_road is False:
                                            #             if word_road in roads:
                                            #                 flag_address_road = address_road_t[___]

                                            # coords.append([address_road[:address_road.index(', ')]])
                                            # coords.append([flag_address_road])

                                            # if address_road != "''":
                                            #     coords.append([address_road])

                                            coords.append([article_sentences[flag_address].lower()])

                                        except Exception as ee:
                                            print("error in address_road:", [long,lat], ee)

                                    else:
                                        coords.append([float(long), float(lat)])

                    except Exception as e:
                        print("error in driver1:", article, e)

                # time.sleep(5)

            coords_t = []
            for item in coords:
                if (item not in coords_t) and (item != ''):
                    coords_t.append(item)

            if len(coords_t) != 0:
                dictionary = {}
                dictionary['coords'] = coords_t
                dictionary['link'] = link
                dictionary['date'] = date
                dictionary['sno'] = sno

                print(dictionary)

                with open("coords_data.json", "a") as outfile:
                    json.dump(dictionary, outfile)

                # dict_list.append(dictionary)

# with open("coords_data.json", "a") as outfile:
#     json.dump(dict_list, outfile)