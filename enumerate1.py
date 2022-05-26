s=input().split(' ')
#print(s)
a=list(map(int,s))
#print(a)
for _,v in enumerate(a):
    print(v**2, end=' ')