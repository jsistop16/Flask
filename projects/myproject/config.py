import os

BASE_DIR = os.path.dirname(__file__)

SQLALCHEMY_DATABASE_URI = 'sqlite:///{}'.format(os.path.join(BASE_DIR, 'pybo.db'))
#db접속주소
#pybo.dp라는 db파일을 루트디렉토리에 저장한다는 뜻
SQLALCHEMY_TRACK_MODIFICATIONS = False