def show_menu(func):
    def prr(*args, **kwargs):
        lis=func(*args, **kwargs)
        for i in range(len(lis)):

            print(f'{i+1}. {lis[i]}')
    return prr

@show_menu
def get_menu(s):
    return list(s.split())


get_menu('Главная Добавить Удалить Выйти')
