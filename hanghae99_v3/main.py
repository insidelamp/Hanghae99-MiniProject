from flask import Flask , render_template , request , jsonify
from pymongo import MongoClient
import certifi

ca = certifi.where()
client = MongoClient('',tlsCAFile=ca)
db = client.notflix

#__init__.py 파일에선 app 객체를 선언하고 각종 모듈, 데이터베이스, 블루프린트 등 값을 설정한다

from . import index       #from . import main : main.py의 내용을 호출하겠다.
from . import calender


app = Flask(__name__)

app.register_blueprint(app.blueprint) # (main.blueprint) main.py에서 사용할 blueprint객체를 blueprint로 설정할거야
app.register_blueprint(link.blueprint)
