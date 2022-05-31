def correct(s: str):
    result = 'ДА'
    corlist = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_0987654321@.'
   # print(corlist)

    if s.count('@')==0 or s.count('.')==0:
        result = "НЕТ"
    for i in s:
        if i not in corlist:
            result = "НЕТ"
    print(result)


correct(input())


# Верное решение #508754648
# Python 3
# # put your python code here
# def check_mail(mail):
#     allow = set("abcdefghijklmnopqrstuvwxyz0123456789_@.")
#     nesessary = {"@", "."}
#     print("ДА") if nesessary <= mail <= allow else print("НЕТ")
#
#
# msg = set(input().lower())
# check_mail(msg)