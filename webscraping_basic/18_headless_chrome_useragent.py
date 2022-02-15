from selenium import webdriver

options = webdriver.ChromeOptions()
options.headless = True 
options.add_argument("window-size=1920x1080") # 이 사이즈로 내부적으로 띄워서 작업
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.82 Safari/537.36")
# 서버의 입장에서 headlessChrome의 경우 이 브라우저의 접속을 막을수 있다, useragent값을 설정해줘야
browser = webdriver.Chrome(options=options)
browser.maximize_window()

url = "https://www.whatismybrowser.com/detect/what-is-my-user-agent"
browser.get(url)

# Mozilla/5.0 (Windows NT 10.0; Win64; x64)
# AppleWebKit/537.36 (KHTML, like Gecko) 
# Chrome/98.0.4758.82 Safari/537.36
detected_value = browser.find_element_by_id("detected_value")
print(detected_value.text)
browser.quit()