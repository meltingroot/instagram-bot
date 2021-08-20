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


# login
driver.get('https://www.instagram.com/accounts/login/')
sleep(5)
driver.find_element_by_css_selector('[name=username]').send_keys(login_id)
sleep(3)
driver.find_element_by_css_selector('[name=password]').send_keys(login_password)
sleep(3)
driver.find_element_by_css_selector('[name=password]').send_keys(Keys.ENTER)
sleep(3)


# tag 검색
print("검색 시작")
driver.get('https://www.instagram.com/explore/tags/%EA%B0%95%EC%95%84%EC%A7%80/')
sleep(10)
print("검색 완료")


# 인기게시물 삭제
driver.execute_script("""
    for (var i; i < 9; i++) {
        document.getElementsByTagName("a")[i].remove();
    } 
""")
print("인기 게시물 삭제 완료")


# 게시물 높이 확인 (scroll 계산 용도)
# driver.execute_script("""
#     return document.getElementsByTagName("a")[0].parentElement.offsetHeight
# """)

# element 확인
element = driver.find_elements_by_tag_name('a')[0]
print("element 확인 완료")


# 최대 처리 건 수
maxCount = 1 

# 처리 건 수
count = 100
elementSequence = 0
while (count <= maxCount) :
    
    imageUrl = element.get_attribute("href")
    print(str(count) + ' : ' + imageUrl)

    if (imageUrl.find("/p/") < 0) :
        break

   
    # 다음 순번 element 선택
    elementSequence = elementSequence + 1
    if (elementSequence > 2) :
        elementSequence = 0

        parentNode = element.find_element_by_xpath('..').find_element_by_xpath('..')

        next_sibling = driver.execute_script("""
            return arguments[0].nextElementSibling
        """, parentNode)

        element = next_sibling.find_elements_by_tag_name('a')[0]

    else :
        parentNode = element.find_element_by_xpath('..')

        next_sibling = driver.execute_script("""
            return arguments[0].nextElementSibling
        """, parentNode)

        element = next_sibling.find_element_by_tag_name('a')

    count = count + 1

    # element = elements[elementSequence]

    # imageUrl = element.get_attribute("href")
    # print(str(count) + ' : ' + imageUrl)


    # if (imageUrl.find("/p/") < 0) :
    #     driver.execute_script("""
    #         window.scrollTo(0,5000);
    #     """)
    #     sleep(5)
    #     driver.execute_script("""
    #         window.scrollTo(0,0);
    #     """)
    #     sleep(5)

    # else : 
    #     driver.execute_script("""
    #         document.getElementsByTagName("a")[0].remove();
    #     """)

    #     if (elementSequence%9 == 0) : 
    #         driver.execute_script("""
    #             window.scrollTo(0,5000);
    #         """)
    #         sleep(1.5)
    #         driver.execute_script("""
    #             window.scrollTo(0,0);
    #         """)
    #         sleep(1.5)
    #         elements = driver.find_elements_by_tag_name('a')
    #         elementSequence = 0
        
    #     elementSequence = elementSequence + 1

    count = count + 1

print("process finish")




