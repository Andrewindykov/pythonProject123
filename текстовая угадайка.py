import random
N=random.randint(10,99)
print(N)    #50
#x=int(input('Введите число ')) #40
i=0
menee=10
bolee=99
x = random.randint(menee, bolee)
print(f"думаю что {x}")
while x!=N:
    if x<N:
        print('нет это число меньше задуманного')
        menee=x+1
        x = random.randint(menee, bolee)
        print(f"думаю что {x}")
    else:
        print('нет это число больше задуманного')
        bolee=x-1
        x = random.randint(menee,bolee)
        print(f"думаю что {x}")
  #  x=int(input('НЕТ! Введите другое число '))
    i+=1
print(f"Ура! угадал с {i} попыток")