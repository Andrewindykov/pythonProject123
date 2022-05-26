sum=0
x=1
znak=1
for i in range(1,int(input("N="))+1):
    x=x*i
    sum+=x*znak
    znak*=(-1)
 #   print(i,x, sum)

print(sum)
