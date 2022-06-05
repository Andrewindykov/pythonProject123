def soort(func):
    def prr(*args, **kwargs):
        lis = func(*args, **kwargs)
        lis.sort()
        return lis
    return prr

@soort
def get_list(s):
    return list(map(int, s.split()))


lst = get_list(input())
print(*lst)
