## With 구름 IDE

from flask import Flask
from sqlalchemy import create_engine, text
application = Flask(__name__)

# DB Info
user = 'root'
password = '000000'
database = 'app'
host = 'localhost'
port = 3306
dbUri = f'mysql+mysqlconnector://{user}:{password}@{host}:{port}/{database}?charset=utf8'
db = create_engine(dbUri, encoding='utf-8', max_overflow=0)

@application.route("/")
def hello():
    return "Hello goorm!"

@application.route('/dbs')
def dbs():
    rows = db.execute(text('SELECT * FROM tableName')).fetchall()
    print(rows)
    return 'dbs' if not rows else str(rows)

@application.route('/dbs/create/<string:name>')
def dbinsert(name):
    data = {'data':name}
    sql = text("INSERT INTO tableName (name) VALUES (:data)")
    rows = db.execute(sql,data).lastrowid
    print(rows)
    return 'complete!' if not rows == 0 else "faile"


if __name__ == "__main__":
    application.run(host='127.0.0.1', port=int(80))
