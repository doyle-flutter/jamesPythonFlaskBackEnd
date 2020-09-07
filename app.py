from flask import Flask
from sqlalchemy import create_engine, text
application = Flask(__name__)

user = 'root'
password = '000000'
database = 'fapp'
host = 'localhost'
port = 3306
dbUri = f'mysql+mysqlconnector://{user}:{password}@{host}:{port}/{database}?charset=utf8'
db = create_engine(dbUri, encoding='utf-8', max_overflow=0)

@application.route("/", methods=['GET'])
def hello():
    return "Hello goorm!"

@application.route('/dbs')
def dbs():
    rows = db.execute(text('SELECT * FROM fdata')).fetchall()
    print(rows)
    return 'dbs' if not rows else str(rows)

@application.route('/dbs/create/<string:name>')
def dbinsert(name):
    data = {'data':name}
    sql = text("INSERT INTO fdata (name) VALUES (:data)")
    rows = db.execute(sql,data).lastrowid
    print(rows)
    return 'complete!' if not rows == 0 else "faile"

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
    application.run(host='172.17.0.31', port=int(80))
