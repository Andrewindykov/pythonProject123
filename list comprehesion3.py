N = [15, 18, 2, 22, 5, 100, 500, 800, -5, -25]
M = [18, 30, 1, 22, 5, 100, 500, 800, -5, -25]

print(N,M,sep='.')
print('----------------')
print(len(N))

lst =  [N[i]+M[i] for i in range(len(N))]

print(lst)
print(*lst)


