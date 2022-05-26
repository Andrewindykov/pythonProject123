s=input()
s2=''
for i in range(len(s)-2):
    if s[i:i+2]=='ра':
        s2+=str(i)+' '

if s2=='': print(-1)
else: print(s2[:-1])