def decorator1(func):#데코레이터1
    def inner():
        print('decorator1')
        func()
    return inner

def decorator2(func):#데코레이터2
    def inner():
        print('decorator2')
        func()
    return inner

@decorator1
@decorator2#여기서부터 @decorator1에 다 들어감
def hello():#데코레이터로 꾸며줄 함수(어떻게 보면 메인함수)
    print('hello')


hello()

##출력값은 decorator1 hello decorator2 hello가 아닌
##decorator1 decorator2 hello가 됨
