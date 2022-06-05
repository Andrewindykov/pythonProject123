def outerf(tp):

    def innerf(s):
        data=s.split()
        data2=map(int,data)
  #      print(data, data2)
        if tp=='list':
            return list(data2)
        else:
            return tuple(data2)

    return innerf


a= outerf(input())
lst=a(input())
print(lst)

