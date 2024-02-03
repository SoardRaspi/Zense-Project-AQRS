from selenium import webdriver
import time

place = input("Enter the place:")

url = "https://www.google.com/maps/place/" + place
driver = webdriver.Chrome()

driver.get(url)
time.sleep(10)

get_url = driver.current_url

print(get_url)
