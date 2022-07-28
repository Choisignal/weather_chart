from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
import urllib.request
import base64
import datetime
import numpy as np

def rader():
    options = webdriver.ChromeOptions()
    options.add_argument("headless")

    browser = webdriver.Chrome(options=options)
    browser.get("http://radar.kma.go.kr/radar/main2.do")
    base64_image = browser.execute_script(
        "return document.querySelector('canvas').toDataURL('image/png').substring(21);")
    output_image = base64.b64decode(base64_image)
    path = "./image/"
    file_name = "rader.png"
    with open(path + file_name, 'wb') as f:
        f.write(output_image)
    browser.quit()

def warn():
    options = webdriver.ChromeOptions()
    options.add_argument("headless")

    driver = webdriver.Chrome(options=options)
    driver.get("https://www.weather.go.kr/w/weather/warning/status.do#")
    driver.implicitly_wait(5)

    r = driver.page_source
    soup = BeautifulSoup(r, "html.parser")
    images_original = driver.find_elements(By.TAG_NAME, "img")
    tits_original = driver.find_elements(By.CLASS_NAME, "tit")
    text_list = []
    for tit in tits_original:
        if tit.text != "":
            text_list = text_list + [tit.text]
    text_list = np.array(text_list)
    p1_start = np.where(text_list == '특보 내용')[0][0]
    p1_end = np.where(text_list == '<참고사항>')[0][0]
    p2_start = np.where(text_list == '기상정보\n+ 더보기')[0][0] + 1
    p2_end = np.where(text_list == '날씨해설')[0][0]
    p1 = ""
    for p in text_list[p1_start:p1_end]:
        p1 += p
    p1 = p1.replace('특보 내용', '특보 내용\n')

    p2 = ""
    for p in text_list[p2_start:p2_end]:
        p2 += p

    images = [img.get_attribute('src') for img in images_original]

    warn = images[6]
    pre_warn = images[7]
    urllib.request.urlretrieve(warn, "./image/warn.png")
    urllib.request.urlretrieve(pre_warn, "./image/pre_warn.png")
    driver.quit()
    return p1, p2

def satellite():
    options = webdriver.ChromeOptions()
    options.add_argument("headless")

    driver = webdriver.Chrome(options=options)
    driver.get("https://www.weather.go.kr/w/image/sat/gk2a.do")
    driver.implicitly_wait(5)

    r = driver.page_source
    soup = BeautifulSoup(r, "html.parser")
    element = driver.find_elements(By.TAG_NAME, "img")
    images = [img.get_attribute('src') for img in element]

    true = images[6]
    day_night = true.replace("true", "daynight")
    urllib.request.urlretrieve(true, "./image/true.png")
    urllib.request.urlretrieve(day_night, "./image/day_night.png")
    driver.quit()

def sfc():
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
    links = [link1, link2, link3]
    for link in links:
        try:
            urllib.request.urlretrieve(link, "./image/sfc3.png")
            break
        except:
            pass

def aws(data_type="temp"):
    now = datetime.datetime.now()
    tag = f"{str(now.hour).zfill(2)}{str(now.minute).zfill(2)[0]}"
    now = now - datetime.timedelta(minutes=(now.minute % 5))

    dates = []
    for delta_time in range(0, 25, 5):
        now = now - datetime.timedelta(minutes=5)
        date = f"{now.year}{str(now.month).zfill(2)}{str(now.day).zfill(2)}{str(now.hour).zfill(2)}{str(now.minute).zfill(2)}"
        dates += [date]

    if data_type == "temp":
        link1 = "https://www.weather.go.kr/img/aws/aws_mtv_"
        link2 = "_460_A0_CENSN_"
        link3 = "_M.png"
    elif data_type == "rain":
        link1 = "https://www.weather.go.kr/img/aws/aws_mrh_"
        link2 = "_460_A0_CENSN_"
        link3 = "_M.png"

    for date in dates:
        try:
            link = f"{link1}{date}{link2}{tag}{link3}"
            urllib.request.urlretrieve(link, f"./image/aws_{data_type}.png")
            break
        except:
            pass

if __name__ == "__main__":
    rader()
    warn()
    satellite()
    sfc()