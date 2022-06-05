def filter_lst(it, key=None):
    if key is None:
        return tuple(it)
    res = ()
    for x in it:
        if key(x):
            res += (x,)
    return res

a = list(map(int, input().split()))

lst = filter_lst(a, lambda x: True) # всё
print(*lst)


lst = filter_lst(a, lambda x: x < 0)  # меньше
print(*lst)

lst = filter_lst(a, lambda x: x >= 0)
print(*lst)

lst = filter_lst(a, lambda x: 3 <=  x <= 6)
print(*lst)
