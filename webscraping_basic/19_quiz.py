# requests를 이용해서 페이지의 상태를 본다, selenium이 필요한지
import requests
from bs4 import BeautifulSoup

url = "https://search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&query=%EC%86%A1%ED%8C%8C+%ED%97%AC%EB%A6%AC%EC%98%A4%EC%8B%9C%ED%8B%B0+%EB%A7%A4%EB%A7%A4&oquery=%EC%86%A1%ED%8C%8C+%ED%97%AC%EB%A6%AC%EC%98%A4%EC%8B%9C%ED%8B%B0&tqi=hlx5vdp0Jy0ssv2LCahssssstvd-278382"

res = requests.get(url)
res.raise_for_status()
soup = BeautifulSoup(res.text, "lxml") 

# soup 객체에 들어있는 파일을 html로 만든 후 안에 원하는 정보 있는지 확인
# with open("quiz.html", "w", encoding="utf8")as f:

data_rows = soup.find("table", attrs={"class":"tb1"}).find("tbody").find_all("tr")
for index, row in enumerate(data_rows):
    columns = row.find_all("td")

    print("========== 매물 {} ==========".format(index=1))
    print("거래 :", columns[0].get_text().strip())
    print("면적: ", columns[1].get_text().strip(), "(공급/전용")
    print("거래: ", columns[2].get_text().strip(), "(만원")
    print("동: ", columns[3].get_text().strip())
    print("층: ", columns[4].get_text().strip())

