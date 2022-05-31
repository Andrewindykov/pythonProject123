import time
def get_nod(a, b):
    """ Вычисление НОД для 2 натуральных чисел медленным алгоритмом Евклида
    :param a: N
    :param b: N
    :return: НОД
    """
    i=0
    while a != b: # Пока а не равно b
        if a > b: # если а юольше б
            a -= b  # из а вычесть б a=a-b
        else:
            b -= a
        i+=1
        if i%1000 == 0 :
            print('.',end='')
    print(f"i={i}")
    return a


def test_nod(func):
    # тест 1 ------------
    a = 28
    b = 35
    res = func(a,b)
    if res == 7:
        print('test 1 ok')
    else:
        print('test 1 fail')

    # тест 2 ------------
    a = 100
    b = 1
    res = func(a, b)
    if res == 1:
        print('test 2 ok')
    else:
        print('test 2 fail')
    # тест 3 ------------
    a = 2
    b = 5000000
    st=time.time()
    res = func(a, b)
    et=time.time()
    dt=et-st
    if res == 2 and dt<0.3:
        print('test 3 ok')
    else:
        print('test 3 fail', 'dt=', round(dt,3))

test_nod(get_nod)

