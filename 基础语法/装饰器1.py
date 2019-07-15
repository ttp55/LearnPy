import functools
def log(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args,**kw):
            print('%s %s():'% (text,func.__name__))
            return func(*args,**kw)
        return wrapper
    return decorator
@log('666')
def now():
    print('2019')
now()
print(now.__name__)