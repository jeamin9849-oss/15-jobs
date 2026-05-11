import requests
from bs4 import BeautifulSoup

keyword="파이썬"
url = f"https://search.incruit.com/list/search.asp?col=job&kw={keyword}&startno=0"
response = requests.get(url)
# print(response.text)

soup = BeautifulSoup(response.text, "html.parser")

lis = soup.find_all("li", class_="c_col")   # 웹내 특정 디자인을 가져오는 명령, css중 c_col이라는 명이 담긴걸 모두 가져옴
# print(len(lis))
# print(lis[0])



for li in lis[0:1]:
    # company = li.find("a", class_="cpname").text.strip() # text.strip :  원하는 텍스트만 출력+공백 제거
    # print(company)
    # title = li.find("div", class_="cell_mid").find("div", class_= "cl_top").find("a").text #cell_mid테그 안에 cl_top 안에 a 테그 안에 텍스트
    # print(title)
    # location = li.find("div", class_="cl_md").find_all("span")[0].text.strip()
    # print(location)
    link = li.find("div", class_= "cell_mid").find("div", class_ = "cl_top").find("a").get("href")
    print(link)