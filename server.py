#
#
#    Flask - Python
#
#

#-*- coding: utf-8 -*-
from flask import Flask
# from sqlalchemy import create_engine, text
application = Flask(__name__)

import socketio
sio = socketio.Client()
sio.connect('http://192.168.0.2:3000')
@sio.event
def connect():
    print("I'm connected!")
    sio.emit('repy', {'key': '연결 후 이벤트 발송!'})

@sio.on('hiPy')
def on_message(data):
    print(f'I received a message! : {data}')
    sio.emit('repy', {'key': '연결 이벤트 받고 다시 발송'})

dbInfo = { 'user' : 'root', 'password' : '123456', 'database' : 'fapp', 'host' : 'localhost', 'port' : 3306 } 
dbUri = f"mysql+mysqlconnector://{dbInfo['user']}:{dbInfo['password']}@{dbInfo['host']}:{dbInfo['port']}/{dbInfo['database']}?charset=utf8"
# db = create_engine(dbUri, encoding='utf-8', max_overflow=0)

@application.route("/", methods=['GET'])
def hello():
    sio.emit('repy', {'key': f'Flask에서 접속하면 내역을 Node로 발송'})
    return "Flask Server!"

# @application.route('/dbs')
# def dbs():
#     rows = db.execute(text('SELECT * FROM fdata')).fetchall()
#     print(rows)
#     return 'dbs' if not rows else str(rows)

# @application.route('/dbs/create/<string:name>')
# def dbinsert(name):
#     data = {'data':name}
#     sql = text("INSERT INTO fdata (name) VALUES (:data)")
#     rows = db.execute(sql,data).lastrowid
#     print(rows)
#     return 'complete!' if not rows == 0 else "faile"

from flask import request
# /qs?q=123
@application.route("/qs", methods=['GET'])
def helloQs():
    argQs = request.args.get('q')
    print(argQs)
    return f"Hello {argQs}!"

@application.route('/headers', methods=['GET'])
def headerPage():
    ct = request.headers['User-Agent']
    return f"Hi {str(ct)}"

@application.route('/postbody', methods=['POST'])
def postBodyLogic():
    pb = request.form['key']
    return {'key2':pb}

@application.route('/xpostbody', methods=['POST'])
def xPostBodyLogic():
    try:
        ct = request.headers.get('Content-Type')
        if(str(ct) == "application/x-www-form-urlencoded"):
            formData = request.form['key']
            return f'DATA : {formData} !'
        else:
            return "TYPE ERR"
    except:
        return "HEADER ERR"
    

if __name__ == "__main__":
    application.run(debug=True, host='127.0.0.1', port=int(3003))
    # 자신의 Local IP를 확인해주세요
    # MAC : ifconfig
    # Window : ipconfig
    # Port 포트 번호는 Node.js 또는 다른 포트와 충돌이 나지 안도록 설정해주세요

### 가상환경 설정하여 진행해주세요

# 가상환경 : sudo pip3 install virtualenv
# 가상환경 생성 : ./~ virutalenv 생성할폴더명
# -> PATH 미등록시 : /usr/local/bin/virtualenv 생성할폴더명

# 실행 : . ./생성한폴더명/bin/activate
# * 실행 후 터미널 입력 창이 '(폴더명) user ... %' 으로 나타나면 정상입니다

# 종료 : deactivate

#.
#| 폴더 구성
#|-- bin : 패키지 폴더
