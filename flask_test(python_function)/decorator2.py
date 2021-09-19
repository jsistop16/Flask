def bold(func):
    def liner(*args, **kwargs):#매개변수 개수에 제한없음
        return '<b>'+func(*args, **kwargs)+'</b>'
    return liner

def italic(func):
    def line(*args, **kwargs):
        return '<i>'+func(*args, **kwargs)+'</i>'
    return line


@bold
@italic
def write(a, b):
    return a+b


print(write('hello ', 'world'))


@bold
@italic
def write2(a,b,c,d):
    return a+b+c+d

print(write2('hi ' , 'my ', 'name ', 'is'))
