print('test.py __name__:', __name__)

#__name__이 의미하는것: 모듈이름
#test.py라는 파일에서의 모듈이름은 test이므로 test가 출력될거라고 생각하지만 아님
#test.py파일 자체를 실행시킨것이기 때문에 main이라는 이름이 출력됨
#원래는 main이 오는게 맞지만 import한 파일명과의 이름과 혼동되는것을 막기위해서
#import된 파일에서는 모듈이름이오는것으로이해할것
#즉 main이라는 얘기는 그 파일의 모듈이름과 동일 


def add_one(data):
    return data+1
    
def add_two(data):
    return data+2


if __name__ == '__main__': #모듈이 아니라 해당 파일을 직접 실행했을때에만 실행하라는 뜻
    print(add_one(10))
    print(add_two(10))