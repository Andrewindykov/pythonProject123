from functools import reduce

def arg_decorator(start=5):
    def func_decorator(func):
        def wrapper(*args, **kwargs):
            res = start + func(*args, **kwargs)
            return res
        return wrapper
    return func_decorator

@arg_decorator(5)
def strtolist(s: str):
    sum_all = reduce(lambda x, y: x + y, list(map(int, s.split())))
    #return sum(list(map(int, s.split())))
    # print(sum_all)
    return sum_all

print(strtolist(input()))
