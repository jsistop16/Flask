from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

'''
app = Flask(__name__)
#어플리케이션 생성 코드
#__name__:모듈명
#pybo.py라는 모듈이 실행되는 것이므로 pybo가 name이라는 변수에 담기게 됨


@app.route('/')
def hello_pybo():
    return 'Hello, Pybo!'
'''
import config
db = SQLAlchemy()
#db라는 객체 생성
migrate = Migrate()
#migrate라는 객체 생성
#두 객체모두 create_app함수 밖에서 생성
#이유는 함수안에서 생성해주면 다른 모듈에서 불러올수없기떄문에
#모듈은 파일로 이해하면 쉬울듯

def create_app():
    #애플리케이션 팩토리
    app = Flask(__name__)
    app.config.from_object(config)
    #config.py파일의 항목들을 app.config환경변수로 부르기 위해 추가해준 코드

    #ORM
    db.init_app(app)
    migrate.init_app(app, db)
    from . import models

    '''기존코드
    @app.route('/')
    def hello_pybo():
        return 'Hello, Pybo!'
    '''#블루프린트 적용 전

    #블루프린트
    from .views import main_views, question_views, answer_views
    app.register_blueprint(main_views.bp)
    app.register_blueprint(question_views.bp)
    '''hello_pybo함수 대신 블루프린트 사용 
    main_views.py에서 생성한 객체 bp를 등록하면 됨'''
    app.register_blueprint(answer_views.bp)
    return app