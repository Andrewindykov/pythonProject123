lst = list(map(int, input().split()))
print(lst)
lst2=[]
for i, value in enumerate(lst):
 #   lst2.append(value)
    lst2.extend([value,value])
print(*lst2)