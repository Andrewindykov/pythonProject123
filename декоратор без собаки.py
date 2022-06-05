def func_show(func):
    def prr(*args, **kwargs):
        print('Площадь прямоугольника:',func(*args, **kwargs))
    return prr

def get_sq(width, height):
    return width*height




