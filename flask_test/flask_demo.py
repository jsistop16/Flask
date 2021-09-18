import test

print('start.py __name__:', __name__)

#즉 출력되는것은 test가 출력됨
#그리고 이파일(flask.py)에서는 __name__이 의미하는것이 파일 자체를 해석했을때의 이름 이므로 __main__이 출력됨
#즉 결과적으로 test, __main__이 순서대로 출력된다.
#import한 test파일에서는 이름이 main이 아니라 test일것이므로 if문은 실행되지 않음