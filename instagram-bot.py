## login info
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
import python_config
login_id = python_config.getXml('INSTAGRAM_LOGIN_INFO', 'LOGIN_ID')
login_password = python_config.getXml('INSTAGRAM_LOGIN_INFO', 'LOGIN_PASSWORD')
## login info


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import pyautogui

driver = webdriver.Edge("driver/msedgedriver.exe")

driver.get('https://www.instagram.com/accounts/login/')
sleep(10)
driver.find_element_by_css_selector('[name=username]').send_keys(login_id)
sleep(3)
driver.find_element_by_css_selector('[name=password]').send_keys(login_password)
sleep(3)
driver.find_element_by_css_selector('[name=password]').send_keys(Keys.ENTER)
sleep(10)
driver.get('https://www.instagram.com/explore/tags/%EA%B0%95%EC%95%84%EC%A7%80/')
sleep(10)
pyautogui.press('tab',presses=3)
imageUrl = driver.find_element_by_css_selector('[class=focus-visible]').get_attribute("href")
print(imageUrl)




