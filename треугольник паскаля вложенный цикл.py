N=15
P=[]

for i in range(N):
    row = [1]* (i+1)
    for j in range(2,i):
        if j != 0 and j != i:
            row[j]=P[i-1][j-1]+P[i-1][j]
    P.append(row)
print(P)

for r in P:
    print(r)