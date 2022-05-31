def check_password(s:str,chars="$%!?@#"):
    if len(s)<=8: return False
    for c in str(s):
        if c not in chars:
            return False
            break
    else return True

print(check_password('1234567'))