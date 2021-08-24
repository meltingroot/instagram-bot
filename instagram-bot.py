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
    for (var i = 0; i < 9; i++) {
        document.getElementsByTagName("a")[0].remove();
    }
""")
print("인기 게시물 삭제 완료")


# element 확인
element = driver.find_elements_by_tag_name('a')[0]
print("element 확인 완료")


# 최대 처리 건 수
maxCount = 2

# 처리 건 수
count = 1
elementSequence = 0
while (count <= maxCount) :
    
    imageUrl = element.get_attribute("href")
    print(str(count) + ' : ' + imageUrl)

    if (imageUrl.find("/p/") < 0) :
        break

    # 새 탭 열기
    driver.execute_script('window.open("'+ imageUrl + '")')
    print("새 탭 열기")
    sleep(5)

    # 탭 전환
    driver.switch_to_window(driver.window_handles[1])
    print("탭 전환")
    sleep(2)

    # 팔로우
    driver.find_elements_by_tag_name('button')[0].click()
    print("팔로우")
    sleep(5)

    # 좋아요
    driver.find_elements_by_tag_name('section')[1].find_elements_by_tag_name("button")[0].click()
    print("좋아요")
    sleep(5)
    

    # 댓글
    driver.execute_script("document.getElementsByTagName('textarea')[0].value='nice puppy!!'")
    print("댓글작성")
    sleep(5)
    driver.execute_script("document.getElementsByTagName('form')[0].getElementsByTagName('button')[1].click()")
    print("댓글달기")
    sleep(5)

    # 탭 닫기
    driver.close();
    print("탭종료")
    sleep(2)

    # 다음 순번 element 선택
    elementSequence = elementSequence + 1
    if (elementSequence > 2) :
        elementSequence = 0
        try : 
            parentNode = element.find_element_by_xpath('..').find_element_by_xpath('..')

            next_sibling = driver.execute_script("""
                return arguments[0].nextElementSibling
            """, parentNode)

            element = next_sibling.find_elements_by_tag_name('a')[0]

        except Exception as e :
            print("오류발생", e)
            driver.execute_script("""
                window.scrollTo(0, document.body.scrollHeight);
            """)

            sleep(3)
            
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

print("process finish")