cifri = [15, 18, 19, 22, 5, 100, 500, 800, -5, -25]
for i,v in enumerate(cifri):
    print(i,v)
    if 10<= abs(v) <=99:
        cifri[i]=0

print(cifri)