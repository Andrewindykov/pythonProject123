N = input().split()

print(N)
lst =  [[N[i],int(N[i+1])] for i in range(len(N)) if i%2==0]

print(lst)


