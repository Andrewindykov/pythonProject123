def make_tag(tag):
    def wrapped(s):
        return "<"+ tag +">"+s+"</" + tag + ">"
    return wrapped

str1 = input()
a = make_tag('h1')
print(a(str1))