
# С помощью генератора множеств сформировать множество из уникальных слов без учета регистра и длина которых не менее трех символов. Вывести на экран размер этого множества.
lst_in = list(input().lower().split())
#print(lst_in)
se={i for i in lst_in if len(i)>3}
print(len(se))