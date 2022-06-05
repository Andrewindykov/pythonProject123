def pairs(func):
    def prr(*args, **kwargs):
        lis1,lis2 = func(*args, **kwargs)
        dic=dict(zip(lis1,lis2))

        return dic
    return prr

@pairs
def get_lists(s1,s2):
    lis1 = list(s1.split())
    lis2 = list(s2.split())

    return lis1,lis2

s1=input()
s2=input()
d = get_lists(s1,s2)
print(*sorted(d.items()))
