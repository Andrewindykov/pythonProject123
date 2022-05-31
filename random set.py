import random

a = {}
for i in range(100):
    N = random.randint(10, 20)
    print(N, end=' ')
    if N not in a:
        a[N] = 1
    a[N] = a[N] + 1
print(a)
