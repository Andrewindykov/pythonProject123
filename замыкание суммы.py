def counter_add(n):
    def step(dx):
        nonlocal n
        dx += n
        return dx

    return step


k = int(input())
cnt = counter_add(2)
print(cnt(k))
