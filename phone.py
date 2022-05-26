s=input()
b=True
if s[:3]!='+7(' or s[6]!=')' or s[10]!='-' or s[13]!='-': print('НЕТ')
else:
    for i in [3,4,5,7,8,9,11,12,14,15]:
        if not(s[i].isdigit()):
            b=False
            break
        if b==False: break
    else: print('ДА')
if b==False: print('НЕТ')
