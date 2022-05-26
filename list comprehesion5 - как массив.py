import sys
# считывание списка из входного потока
s = sys.stdin.readlines()
lst_in = [list(map(int, x.strip().split())) for x in s]

lst_in.reverse()

lst=[ i[-j-1]
    for i in lst_in
    for j in range(len(i))
      ]

print(*lst)


