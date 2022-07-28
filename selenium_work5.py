#
import time

from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
import urllib.request
from selenium.webdriver.common.action_chains import ActionChains
import pyautogui

options = webdriver.ChromeOptions()
options.add_argument("headless")

driver = webdriver.Chrome()
driver.get("https://www.weather.go.kr/plus/land/current/aws_distribution_popup.jsp")
driver.implicitly_wait(5)

r = driver.page_source


soup = BeautifulSoup(r, "html.parser")
element = driver.find_elements("name","content")[0]
actionChains = ActionChains(driver)
actionChains.context_click(element).perform()
pyautogui.press('down')
pyautogui.press('down')
pyautogui.press('enter')
time.sleep(1)
pyautogui.press('enter')
time.sleep(1)