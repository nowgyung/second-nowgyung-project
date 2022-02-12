import csv
import requests
from bs4 import BeautifulSoup

url = "https://finance.naver.com/sise/sise_market_sum.nhn?sosok=0&page="

filename = "시가총액1-200.csv"
f = open(filename, "w", encoding="utf-8-sig", newline="") # 줄바꿈 엔터를 없애주기 위해서 공백
writer = csv.writer(f) # writer를 이용해서 파일을 쓸 수 있다

title = "N	종목명	현재가	전일비	등락률	액면가	시가총액	상장주식수	외국인비율	거래량	PER	ROE".split("\t") 
#tab으로 구분한 데이터들이 리스트 형태로 / ["N", "종목명", "현재가", ...]
print(type(title))
writer.writerow(title)

for page in range(1, 5): #1페이지부터 4페이지까지
    res = requests.get(url + str(page))
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "lxml")
 
    data_rows = soup.find("table", attrs={"class":"type_2"}).find("tbody").find_all("tr")
    for row in data_rows:
        columns = row.find_all("td")
        if len(columns) <= 1: # 의미 없는 데이터는 skip
           continue
        data = [column.get_text().strip() for column in columns] #한줄 for문 만들기 / td들이 가지고 있는 text정보들이 저장될것 / strip함수를 통해 불필요한것 제거 
        #print(data)
        writer.writerow(data)