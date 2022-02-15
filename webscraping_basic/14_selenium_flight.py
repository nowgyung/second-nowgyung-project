from selenium import webdriver
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
