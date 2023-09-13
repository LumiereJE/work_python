import requests                     # 서버로부터 정보를 요청해서 가져오기, get방식으로 가져 올 예정
from bs4 import BeautifulSoup       # html parser
# url = "https://www.weather.go.kr/weather/observation/currentweather.jsp"
# html = requests.get(url).text
# print(html)
# soup = BeautifulSoup(html, "html.parser")       # 파서 : 어떠한 규칙을 가지고 자르는 도구
# print(soup)

# 날씨 정보 가져 오기
url = "http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=108"

# http Get요청
res = requests.get(url).text

# HTML 파싱
soup = BeautifulSoup(res, "html.parser")
print(soup)

for loc in soup.select("location"):
    print("도시 : ", loc.select_one("city").string)
    print("날씨 : ", loc.select_one("wf").string)
    print("최저기온 : ", loc.select_one("tmn").string)
    print("최고기온 : ", loc.select_one("tmx").string)
    print("-"*20)







