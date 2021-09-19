def mark(tag):
    def outer(function):
        def inner(*args, **kwargs):
            print('<{0}>'.format(tag)+function(*args, **kwargs)+'</{0}>'.format(tag))
        return inner
    return outer

@mark('b')
def bold(title):
    return title

@mark('h1')
def title(title):
    return title


print(title("안녕하쇼"))
