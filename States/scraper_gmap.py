import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
import csv
import time
import os
import json

H = []

curr_path = os.path.join(os.getcwd(), 'Maharashtra')

dic_list = []

driver = webdriver.Chrome('./chromedriver')
# driver.get("https://timesofindia.indiatimes.com/topic/Road-accident/news/" + str(count))

# try:
with open(os.path.join(curr_path, 'content3.csv'), mode='r') as file:
    csvFile = csv.reader(file)
    csvFile = list(csvFile)

    # for i in range(1, len(csvFile)):
    for i in range(1, 2):
        try:
            sno, h, link, date = csvFile[i]
            h = h[1:len(h) - 1]
            h = h.split(',')

            for i in range(len(h)):
                h[i] = h[i].strip(" ")[1:len(h[i]) - 1]

            # print(h)

            for i in range(len(h)):
                driver.get("https://developers-dot-devsite-v2-prod.appspot.com/maps/documentation/utils/geocoder#q%3D" + str(h[i]))

                # articles = driver.find_elements(By.CLASS_NAME, "result-formatted-address")[0]
                # articles = driver.find_elements(By.XPATH, '//*[@id="result-0"]/table/tbody/tr/td[2]/p[2]')

                time.sleep(3)

                articles = driver.find_elements(By.XPATH, '//p[@class="result-formatted-address"]')[0]

                print(h[i], ":", articles.get_attribute("innerText"))

                # if 'Maharashtra' in articles:
                #     headings = driver.find_elements(By.CLASS_NAME, "result-location")[0]

        except Exception as e:
            print("some error occurred:", e)

# with open("coords_data3.json", "w") as outfile:
#     json.dump(dic_list, outfile)
