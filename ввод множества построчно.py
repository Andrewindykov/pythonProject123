a=input().lower().strip()
s=set()
s.add(a)
while a!='q':
    a=input().lower().strip()
    s.add(a)
s.remove('q')
print(len(s))