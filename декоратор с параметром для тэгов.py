def arg_decorator(tag='h1'):
    def func_decorator(func):
        def wrapper(*args, **kwargs):
            res = '<'+tag+'>'+ func(*args, **kwargs)+'</'+tag+ '>'
            return res
        return wrapper
    return func_decorator

@arg_decorator('div')
def strtolower(s: str):
    return s.lower()

print(strtolower(input()))
