from selenium import webdriver

# 원하는 값을 발견할때 까지 먼저 끝내 않도록 설정
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser =  webdriver.Chrome()
browser.maximize_window() # chrome 창을 띄우고 최대화로

url = "https://flight.naver.com/"
browser.get(url) # url로 이동

# 가는 날 선택 클릭
browser.find_element_by_link_text("가는 날").click()


# 이번 달 27일, 28일 선택
#browser.find_elements_by_link_text("27")[0].click() #[0] -> 이번 달
#browser.find_elements_by_link_text("28")[0].click() #[0] -> 이번 달

# 다음 달 27일, 28일 선택
#browser.find_elements_by_link_text("27")[1].click() #[1] -> 다음 달
#browser.find_elements_by_link_text("28")[1].click() #[1] -> 다음 달

# 이번달 27일, 다음 28일 선택
browser.find_elements_by_link_text("27")[0].click() #[0] -> 이번 달
browser.find_elements_by_link_text("28")[1].click() #[1] -> 다음 달

# 제주도 선택
browser.find_elemnet_by_xpath("//*[@id='__next']/div/div[1]/div[4]/div/div/div[2]/div[1]/button[2]/b").click()

# 항공권 검색 클릭
browser.find_element_by_link_text("항공권 검색").click()

try:
    elem = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, "//*[@id='__next']/div/div[1]/div[4]/div/div[2]/div[2]/div/button")))
# 성공햇을 때 동작 수행
# webdriverwait를 통해 브라우저를 최대 10초동안 기다린다 10초안에 발생되면 바로 진행 xpath기준으로 ""에 해당하는 element가 나올때 까지  / 어떤 element가 위치할 때 까지 기다려 달라
    print(elem.text) # 첫 번째 결과 출력
finally:
    browser.quit()

# 첫 번째 결과 출력
#element = browser.find_element_by_xpath("//*[@id='__next']/div/div[1]/div[4]/div/div[2]/div[2]/div/button")
#print(elem.text)


# a 태그가 보이지 않아 진행하지 못함, 진행과정은 기록
