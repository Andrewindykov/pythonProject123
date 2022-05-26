def simple_map(transformation, values):
    p=[]
    for i in values:
        p.append(transformation(i))
   # print(p)
    return p
values=[1,2,1,5,7]
print(*simple_map(lambda x:x+5, values))


