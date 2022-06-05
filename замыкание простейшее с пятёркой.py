# put your python code here
k = int(input())

def counter_add():
    five=5
    def step(b):
        nonlocal five
        return b+five
    return step


cnt=counter_add()
print(cnt(k))
