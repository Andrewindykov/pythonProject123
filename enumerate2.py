lst = list(map(int, input().split()))

for i, value in enumerate(lst):
    lst[i] = value ** 2

print(*lst)