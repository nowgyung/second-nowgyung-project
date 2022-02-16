import requests
from bs4 import BeautifulSoup


#오늘의 날씨 정보고 가져오기

def scrape_weather():
    print("[오늘의 날씨]")
    url = "https://search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&query=%EC%84%9C%EC%9A%B8+%EB%82%A0%EC%94%A8&oquery=%ED%8C%8C%EC%9D%B4%EC%8D%AC+scrape_weather&tqi=hlxOFlprvOssskBKn9hssssssho-070998"

    res = requests.get(url)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "lxml")
    # 흐림, 어제보다 OO° 높아요
    cast = soup.find("p", attrs={"class":"summary"}).get_text()
    # 현재, OO°C (최저 OO° / 최고 OO° )
    curr_temp = soup.find("div", attrs={"class":"temperature_text"}).get_text() # 현재 온도
    min_temp = soup.find("span", attrs={"class":"lowest"}).get_text().replace("최저기온", "") # 최저 온도
    max_temp = soup.find("span", attrs={"class":"highest"}).get_text().replace("최고기온", "") # 최고 온도
    # 오전 강수확률 OO% / 오후 강수확률 OO%
    #morning_rain_rate = soup.find("span", attrs = {"class":"weather_left"}).get_text().replace("오전", "") # 오전 강수확률
    #afternoon_rain_rate = soup.find("span", attrs = {"class":"weather_left"}).get_text().replace("오후", "") # 오후 강수확률 / 개발자 모드 이름이 똑같이 되어있음
    # weather = soup.find("div", attrs = {"class":"cell_weather"}).get_text
    # morning_rain_rate = weather.find_all("weather_inner")[0].get_text # 오전 강수확률
    # afternoon_rain_rate = weather.find_all("weather_inner")[1].get_text # 오후 강수확률

    # 미세먼지 OO /좋음
    # 초미세먼지 OO / 좋음
    dust = soup.find("ul", attrs = {"class":"today_chart_list"}).get_text()
    pm10 = dust.find_all("li")[0].get_text() # 미세먼지
    pm25 = dust.find_all("li")[1].get_text() # 초미세먼지

    

 # 출력
    print(cast)
    print("현재 {} (최저 {} / 최고 {})".format(curr_temp, min_temp, max_temp))
    print("오전 {} / 오후 {}".format(morning_rain_rate, afternoon_rain_rate))
    print() # 줄 바꿈
    print("미세먼지 {}".format(pm10))
    print("초미세먼지 {}".format(pm25))
    print()

if __name__ == "__main__":
    scrape_weather() #직접 실행시 동작