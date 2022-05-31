def check_password(s:str,chars="$%!?@#"):
    if len(s)<8: return False
    for c in str(s):
        if c in chars:
            return True
            break
    else:
        return False

print(check_password('12345d67#'))