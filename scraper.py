import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
import csv
import time

count = 432
sno = 10254

H = []

driver = webdriver.Chrome('./chromedriver')
# driver.get("https://timesofindia.indiatimes.com/topic/Road-accident/news/" + str(count))

fields = ['SNo.', 'Heading', 'Sub-Heading', 'Link']
filename = "all_articles_raw.csv"

with open(filename, 'a') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(fields)

# try:
if True:
    while True:
        driver.get("https://timesofindia.indiatimes.com/topic/Road-accident/news/" + str(count))

        articles = driver.find_elements(By.CLASS_NAME, "uwU81")
        headings = driver.find_elements(By.XPATH, '//div[@class="fHv_i o58kM "]')
        sub_headings = driver.find_elements(By.XPATH, '//p[@class="oxXSK o58kM"]')

        try:
            print("ðððððððððððððððððððððððððððððð")
            print("no error at page:", count)
            print("ðððððððððððððððððððððððððððððð")

            for i in range(len(articles)):
                # print("heading:", headings[i].text)
                # print("sub-heading:", sub_headings[i].text)
                # print("link:", articles[i].find_element(By.TAG_NAME, "a").get_attribute("href"))
                # print("------------------------------")

                h = headings[i].text
                sub_h = sub_headings[i].text
                link = articles[i].find_element(By.TAG_NAME, "a").get_attribute("href")

                print("heading:", h)
                print("sub-heading:", sub_h)
                print("link:", link)
                print("------------------------------")

                if (link[36:40] == 'city') and (h not in H):
                    H.append(h)

                    with open(filename, 'a') as csvfile:
                        csvwriter = csv.writer(csvfile)
                        csvwriter.writerow([sno, h, sub_h, link])

                    sno += 1

            count += 1

        except Exception as ee:
            # driver.close()
            print("error in inner block:", ee)

            print("ßßßßßßßßßßßßßßßßßßßßßßßßßßßßßß")
            print("error at page:", count)
            print("ßßßßßßßßßßßßßßßßßßßßßßßßßßßßßß")

            # print("articles:", len(articles), articles)
            # print("headings:", len(headings), headings)
            # print("sub_headings:", len(sub_headings), sub_headings)

            count += 1

        time.sleep(0.2)

# except Exception as e:
#     print("some error occurred:", e)
