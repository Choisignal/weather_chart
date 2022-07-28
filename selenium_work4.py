#
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
import urllib.request
import datetime

dt_utc = datetime.datetime.utcnow()
dt_utc = dt_utc - datetime.timedelta(hours=(dt_utc.hour % 3))
dt_utc2 = dt_utc - datetime.timedelta(hours=3)
dt_utc3 = dt_utc - datetime.timedelta(hours=6)
time1 = f"{dt_utc.year}{str(dt_utc.month).zfill(2)}{str(dt_utc.day).zfill(2)}{str(dt_utc.hour).zfill(2)}"
time2 = f"{dt_utc2.year}{str(dt_utc2.month).zfill(2)}{str(dt_utc2.day).zfill(2)}{str(dt_utc2.hour).zfill(2)}"
time3 = f"{dt_utc3.year}{str(dt_utc3.month).zfill(2)}{str(dt_utc3.day).zfill(2)}{str(dt_utc3.hour).zfill(2)}"
link1 = f"https://www.weather.go.kr/w/repositary/image/cht/img/sfc3_{time1}.png"
link2 = f"https://www.weather.go.kr/w/repositary/image/cht/img/sfc3_{time2}.png"
link3 = f"https://www.weather.go.kr/w/repositary/image/cht/img/sfc3_{time3}.png"
links = [link1,link2,link3]
for link in links:
    try:
        urllib.request.urlretrieve(link, "./image/sfc3.png")
        break
    except:
        pass
