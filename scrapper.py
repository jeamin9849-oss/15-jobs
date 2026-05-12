import requests
from bs4 import BeautifulSoup

def search_incruit(keyword,pages):


    jobs = []
    for i in range(pages):
        page = i * 30
        url = f"https://search.incruit.com/list/search.asp?col=job&kw={keyword}&startno={page}"

        response = requests.get(url)

        soup = BeautifulSoup(response.text, "html.parser") #BeautifulSoup라는 class를 통해 soup라는 객체를 만듬

        lis = soup.find_all("li", class_="c_col")   # 웹내 특정 디자인을 가져오는 명령, css중 c_col이라는 명이 담긴걸 모두 가져옴
        # print(len(lis))
        # print(lis[0])



        for li in lis:
            company = li.find("a", class_="cpname").text.strip() # text.strip :  원하는 텍스트만 출력+공백 제거
            # print(company)
            title = li.find("div", class_="cell_mid").find("div", class_= "cl_top").find("a").text #cell_mid테그 안에 cl_top 안에 a 테그 안에 텍스트
            # print(title)
            location = li.find("div", class_="cl_md").find_all("span")[0].text.strip()
            # print(location)
            link = li.find("div", class_= "cell_mid").find("div", class_ = "cl_top").find("a").get("href") #...에서 get함수로 href 의 내용을 가져옴
            # print(link)
            
            job_data = {
                "company" : company,
                "title" : title,
                "location" : location,
                "link" : link        
            }

            jobs.append(job_data)

            
    return jobs

# def search_saramin(keyword,pages):
#     url = f"https://www.saramin.co.kr/zf_user/search/recruit?search_area=main&search_done=y&search_optional_item=n&searchType=search&searchword=%ED%8C%8C%EC%9D%B4%EC%8D%AC&recruitPage={page}&recruitSort=relation&recruitPageCount=40&inner_com_type=&company_cd={keyword}&show_applied=&quick_apply=&except_read=&ai_head_hunting=&mainSearch=n"


response = requests.get(url)
print(response.status_code) # status_code는 보통 HTTP 요청 결과 상태를 나타내는 값 200 : 성공, 404 : 페이지 없음
print(response.text)

