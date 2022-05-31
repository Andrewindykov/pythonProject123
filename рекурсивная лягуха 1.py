N=int(input())

def get_path(N):
    if N<=2:
        return(N)
    else:
        return get_path(N-1)+get_path(N-2)
#print('hello')
print(get_path(N))








