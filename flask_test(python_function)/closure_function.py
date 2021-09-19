def type_checker(func):
    def inner(digit1, digit2):
        if type(digit1) != int or type(digit2) != int:
            print('only integer support')
            return
        func(digit1, digit2)
    return inner

@type_checker
def multiple(digit1, digit2):#type_checker함수의 매개변수로 전달
    return print(digit1 * digit2)

multiple(2,4)
multiple(2, '4')
