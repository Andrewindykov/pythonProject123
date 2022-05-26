N = list(map(int,input().split()))
M = list(input().lower().split())
print(N,M,sep='\n')
lst =  [M[i-1] for i in N]
x=' '.join(lst)
print(x.capitalize())

# 4 3 1
# Буря мглою небо кроет