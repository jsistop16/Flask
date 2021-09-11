from flask import Blueprint, url_for
from werkzeug.utils import redirect

bp = Blueprint('main', __name__, url_prefix='/')
#블루프린트 객체생성
#main:이름 / __name__:모듈이름 / url_prefix:URL프리픽스
#총 3개의 매개값 전달(객체 생성시에)

#블루프린트의 용도
#__init__.py파일에서 새로운 url이 추가될떄 마다 직접 추가해주는 수고를 덜고
#main_views.py파일에 bp객체를 생성하고 그 파일에 추가되는 url매핑과 함수들을 추가해주면
#편함

@bp.route('/hello')
#'/(매핑)': ip주소 뒤에 들어가는 식별자 정도로 이해
#bp=blueprint로 생성한 객체
def hello_pybo():
    return 'Hello, Pybo!'

@bp.route('/')
def index():
    return redirect(url_for('question._list'))