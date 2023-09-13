# 플라스크 : 웹 개발을 위한 모듈


from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, Flask!!!'

if __name__ == '__main__':
    app.run()




