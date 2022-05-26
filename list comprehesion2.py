N = list(map(float,input().split()))

print(N)
lst =  [N[i] for i in range(len(N)) if i%2==0]

print(*lst)


