## login info
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
import python_config
login_id = python_config.getXml('INSTAGRAM_LOGIN_INFO', 'LOGIN_ID') #instagram id
login_password = python_config.getXml('INSTAGRAM_LOGIN_INFO', 'LOGIN_PASSWORD') #instagram password
## login info


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import pyautogui

#browser driver
driver = webdriver.Edge("instagram-bot/driver/msedgedriver.exe") 

driver.get('https://www.instagram.com/accounts/login/')
sleep(5)
driver.find_element_by_css_selector('[name=username]').send_keys(login_id)
sleep(3)
driver.find_element_by_css_selector('[name=password]').send_keys(login_password)
sleep(3)
driver.find_element_by_css_selector('[name=password]').send_keys(Keys.ENTER)
sleep(3)
driver.get('https://www.instagram.com/explore/tags/%EA%B0%95%EC%95%84%EC%A7%80/')
sleep(10)

elements = driver.find_elements_by_tag_name('a')

count = 1
maxCount = 300
elementCount = 0
while (count <= maxCount) :
    element = elements[elementCount]

    imageUrl = element.get_attribute("href")
    print(str(count) + ' : ' + imageUrl)

    if (imageUrl.find("/p/") < 0) :
        driver.execute_script("""
            window.scrollTo(0,10000);
        """)
        sleep(10)

    else : 
        driver.execute_script("""
            document.getElementsByTagName("a")[0].remove();
        """)

        if (elementCount%10 == 0) : 
            driver.execute_script("""
                window.scrollTo(0,5000);
            """)
            sleep(3)
            elements = driver.find_elements_by_tag_name('a')
            elementCount = 0
        
        elementCount = elementCount + 1

    count = count + 1

print("process finish")




