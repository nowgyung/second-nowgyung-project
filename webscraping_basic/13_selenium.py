# 웹 페이지 테스트 자동화 프레임워크, 웹 브라우저를 컨트롤 하면서  필요한 작업한다
# 동작속도 늦고 메모리도 차지하는 편, requests와 다르게 동적 웹 페이지 작업 가능
# requests와 selenium html 문서를 가져오는 방식의 차이 일뿐, beautifulsoup을 이용해서 데이터 추출
# 크롬 버전에 맞는 크롬드라이버가 반드시 있어야 한다
# find_element(s)_by_id id로 찾기
# find_element(s)_by_class_name class name으로 찾기
# find_element(s)_by_link_text 링크 text로 찾기
# find_element(s)_by_xpath xpath로 찾기
# click() 클릭
# send_keys() 글자 입력 / 이미 다른 글자가 있다면 clear()로 삭제후 진행


import time
from selenium import webdriver

browser = webdriver.Chrome() # "./chromedriver.exe"

# 1. 네이버 이동
browser.get("http://naver.com") # 크롭 웹 드라이버 객체를 생성, 그 브라우저에서 이 url로 이동

# 2. 로그인 버튼 클릭
elem = browser.find_elemnt_by_class_name("link_login")
elem.click()

#  elem = browser.find_element_by_class_name("link_login") / class이름이  link_login이 element를 가져온다 (로그인 창)
#  elem.click() element 클릭
#  browser.back() 뒤로가기
#  browser.forward() 앞으로 가기
#  browser.refresh() 새고로침
#  elem = browser.find_element_by_id("query") / query인 element를 가져온다 (검색 창)
#  from selenium.webdriver.common.keys import Keys / 글자를 Keys.Enter하기 위해서 다른 모드를 가져와야 한다, KEY 값을 직접 입력할수 있다
#  elem.send_keys("나도코딩") / 글자 입력
#  elem.send_keys(Keys.ENTER) / enter입력

#  for e in elem:
#  ...     e.get_attribute("href") /태그에 해당되는 element들을 다 들고오기
#  ...       / enter 치기             
#  browser.get("http:daum.net") / 브라우저 이동
#  elem = browser.find_element_by_name("q") / name속성에 해당되는 q찾기 (검색버튼)
#  elem = browser.find_element_by_xpath("//*[@id='daumSearch']/fieldset/div/div/button[2]") / xpath를 통한 검색버튼 가져오기
#  elem.click() / 검색실행
#  browser.quit() / 브라우저 전체 창닫기 close는 현재 열린 창만

# 3. id, pw 입력
browser.find_element_by_id("id").send_keys("naver_id")
browser.find_element_by_id("pw").send_keys("password")

# 4. 로그인 버튼 클릭
browser.find_elemnt_by_id("log.login").click()

time.sleep(3)

# 5. id 를 새로 입력
#  browser.find_element_by_id("id").send_keys("my_id")
browser.find_element_by_id("id").clear()
browser.find_element_by_id("id").send_keys("my_id")

# 6. html 정보 출력
print(browser.page_source)

# 7. 브라우저 종료
# browser.close() # 현재 탭 만 종료
browser.quit() # 전체 브라우저 종료