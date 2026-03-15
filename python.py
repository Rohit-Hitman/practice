 ##Flatten a Nested List
data = [[1, 2, [3]], [4, 5], 6]


def flat(data):
    l=[]
    for i in data:
        if isinstance(i,list):
            l.extend(flat(i))
        else:
            l.append(i)
    #print(l)
    return l

res=flat(data)
print(res)


