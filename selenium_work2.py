# 특보
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
import urllib.request
import numpy as np

options = webdriver.ChromeOptions()
options.add_argument("headless")

driver = webdriver.Chrome(options=options)
driver.get("https://www.weather.go.kr/w/weather/warning/status.do#")
driver.implicitly_wait(5)

r = driver.page_source
soup = BeautifulSoup(r, "html.parser")
images_original = driver.find_elements(By.TAG_NAME,"img")
tits_original = driver.find_elements(By.CLASS_NAME,"tit")
text_list = []
for tit in tits_original:
    if tit.text != "":
        text_list = text_list + [tit.text]
text_list = np.array(text_list)
p1_start = np.where(text_list == '특보 내용')[0][0]
p1_end = np.where(text_list == '<참고사항>')[0][0]
p2_start = np.where(text_list == '기상정보\n+ 더보기')[0][0]+1
p2_end = np.where(text_list == '날씨해설')[0][0]
p1 = ""
for p in text_list[p1_start:p1_end]:
    p1 += p
p1 = p1.replace('특보 내용','특보 내용\n')

p2 = ""
for p in text_list[p2_start:p2_end]:
    p2 += p

images = [img.get_attribute('src') for img in images_original]
for image in images:
    print(image)

warn = images[6]
pre_warn = images[7]
urllib.request.urlretrieve(warn, "warn.png")
urllib.request.urlretrieve(pre_warn, "pre_warn.png")