N = list(map(int,input().split()))
M = list(map(int,input().split()))
#print(N,M,sep='\n')
lst =  [N[i]+M[i] for i in range(len(N))]

print(*lst)


