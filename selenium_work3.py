#
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
import urllib.request

options = webdriver.ChromeOptions()
options.add_argument("headless")

driver = webdriver.Chrome(options=options)
driver.get("https://www.weather.go.kr/w/image/sat/gk2a.do")
driver.implicitly_wait(5)

r = driver.page_source
soup = BeautifulSoup(r, "html.parser")
element = driver.find_elements(By.TAG_NAME,"img")
images = [img.get_attribute('src') for img in element]

true = images[6]
day_night = true.replace("true","daynight")
urllib.request.urlretrieve(true, "true.png")
urllib.request.urlretrieve(day_night, "pre_warn.png")
