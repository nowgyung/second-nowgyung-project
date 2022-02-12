import requests
from bs4 import BeautifulSoup

for year in range(2015, 2020):
    url = "https://search.daum.net/search?w=tot&q={}%EB%85%84%EC%98%81%ED%99%94%EC%88%9C%EC%9C%84&DA=MOR&rtmaxcoll=MOR".format(year)
    res = requests.get(url)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "lxml")

    images = soup.find_all("img", attrs={"class":"thumb_img"})
    for idx, image in enumerate(images):
        print(image["src"])
        image_url = image["src"]
        #if image_url.startswith("//"): 
        #   image_url = "https:" + image_url #//로 시작하게 된다면 앞부분에 https를 덧붙임

        #   print(image_url)
        image_res = requests.get(image_url)
        image_res.raise_for_status()

        with open("movie_{}_{}.jpg" .format(year, idx+1), "wb") as f: # 이미지 저장하면서 이름이 겹쳐질수있음
            f.write(image_res.content) # 이미지 소스들을 통해서 파일로 다 저장, 페이지내에 있는 썸네일들이 다 다운로드됨 

            if idx >= 4: #상위 5개 이미지까지만 다운로드
                break