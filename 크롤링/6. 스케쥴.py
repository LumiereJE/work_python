import schedule
import time
import requests
from bs4 import BeautifulSoup

def perform_web_crawling():
    # 웹 크롤링 작업 수행
    url = "http://www.naver.com"
    resp = requests.get(url)
    if resp.status_code == 200:
        soup = BeautifulSoup(resp.text, "html.parser")
    print(soup)

def job():
    print("웹 크롤링을 수행 합니다.")
    perform_web_crawling()

# 매일 정해진 시간에 동작 하도록 구현
schedule.every().day.at("09:47").do(job)

# 프로그램 무한으로 돌리기
while True:
    schedule.run_pending()  # 1초마다 체크
    time.sleep(1)