from pybo import db

class Question(db.Model):#질문 모델 생성하기
    # Question이라는 클래스가 db.Model을 상속받음
    id = db.Column(db.Integer, primary_key=True)
    subject = db.Column(db.String(200), nullable=False)
    content = db.Column(db.Text(), nullable=False)
    create_date = db.Column(db.DateTime(), nullable=False)


class Answer(db.Model):#답변 모델 생성하기
    id = db.Column(db.Integer, primary_key=True)
    question_id = db.Column(db.Integer, db.ForeignKey('question.id', ondelete='CASCADE'))
    #question_id 는 질문모델과 연결하기 위한 용도
    #어떤 질문에 대한 답변인지 알아야할거 아니냐고
    #어떤 데이터 속성을 기존 모델과 연결하려면 외부키(FK)를 사용해야 함
    #ondelete='CASCADE' 질문이 삭제되면 연동되서 답변도 삭제됨
    question = db.relationship('Question', backref=db.backref('answer_set'))
    '''db.relationship에서는 
    첫번째 값: 참조할 모델명(답변이 질문모델을 참조)
    두번쨰 값: 역참조 설정(질문이 답변을 참조)
    '''
    content = db.Column(db.Text(), nullable=False)
    create_date = db.Column(db.DateTime(), nullable=False)