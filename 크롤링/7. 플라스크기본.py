from bs4 import BeautifulSoup
# request → 리액트에서 axios같은 역할을 함
from flask import Flask, jsonify, Response, request
import requests
import json

app = Flask(__name__)

data = {
    'stations' : ['강남역', '역삼역', '서울역'],
    'ridership': [1000, 800, 1200]
}

# GET요청을 처리하는 라우터
@app.route('/api/data', methods=['GET'])
def get_Data():  # 위의 어노테이션이 이 함수를 불러주는 것임
    resp = Response(json.dumps(data, ensure_ascii=False), mimetype='application/json; charset=utf-8')
    return resp # 웹 브라우저에서 요청이 와서 응답을 던져줌
@app.route('/api/weather', methods=['GET'])
def get_weather():
    url = "http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=108"
    # http GET요청
    resp = requests.get(url)
    # http 파싱
    soup = BeautifulSoup(resp.text, "html.parser")
    output = ""
    for location in soup.select("location"):
        output += f"<h3>{location.select_one('city').string}<h3>"
        output += f"날씨 : {location.select_one('wf').string}</br>"
        output += f"최저/최고 기온 : {location.select_one('tmn')}/{location.select_one('tmx')}</hr>"

    return output

@app.route('/api/query', methods=['GET'])
def get_query():
    output = ""
    item_type = request.args.get('type', default=None, type=None)
    item_color = request.args.get('color', default=None, type=None)
    output += f"<h1>{item_type}</h1>"
    output += f"<h1>{item_color}</h1>"
    return output

# 서버 실행
if __name__ == '__main__': # 진입지점이 여기면 플라스크를 띄워라
    app.run(debug=True)