from functools import wraps

def make_blink(function):
    """ This is a decorator function """

    @wraps(function)
    def decorator():
        ret = function()
        return "<blink> " + ret +" </blink>"

    return decorator

def func1():
    """ Original function """
    return "Hello World"

@make_blink
def func2():
    """ Original function wraped in decorator """
    return "Hello World"

print(func1())
print(func1.__name__)
print(func1.__doc__)
print('\n')
print(func2())
print(func2.__name__)
print(func2.__doc__)