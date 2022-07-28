# 레이더
from selenium import webdriver
import base64

# 옵션 생성
options = webdriver.ChromeOptions()
# 창 숨기는 옵션 추가
options.add_argument("headless")

browser = webdriver.Chrome(options=options)
browser.get("http://radar.kma.go.kr/radar/main2.do")
base64_image = browser.execute_script("return document.querySelector('canvas').toDataURL('image/png').substring(21);")
output_image = base64.b64decode(base64_image)
path = "./image/"
file_name = "rader.png"
with open(path + file_name, 'wb') as f:
    f.write(output_image)