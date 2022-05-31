N = int(input())

def get_path(n):
    return n if n in (1, 2) else get_path(n - 1) + get_path(n - 2)

print(get_path(N))








