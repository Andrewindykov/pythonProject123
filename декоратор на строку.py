t = {'ё': 'yo', 'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ж': 'zh',
     'з': 'z', 'и': 'i', 'й': 'y', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p',
     'р': 'r', 'с': 's', 'т': 't', 'у': 'u', 'ф': 'f', 'х': 'h', 'ц': 'c', 'ч': 'ch', 'ш': 'sh',
     'щ': 'shch', 'ъ': '', 'ы': 'y', 'ь': '', 'э': 'e', 'ю': 'yu', 'я': 'ya'}


def nomin(func):
    def prr(*args, **kwargs):
        s = func(*args, **kwargs)
      #  print('d:',s)
        # print(len(s))
        s2 = ''
        for i in range(len(s)):
            if s[i] == s[i - 1] == '-':
                pass
            else:
                s2 += s[i]
        #  print(s2)
        return s2

    return prr


@nomin
def kirlat(s):
    s2 = s.lower()
    s3=''
    print(s2)
    for ch in s2:
        if 'а'<=ch<='я':
            s3+=t[ch]
        elif ch in ': ;.,_':
            s3+='-'
        else:
            s3 += ch
   # print('f:', s3)
    return s3


s = input()

print(kirlat(s))
