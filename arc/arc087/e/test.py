root = 6
d = dict()
last = tuple([0] * (root+1))
d[last] = 0

def calc(x):
    if x in d:
        return d[x]
    
    base = list(x)
    mex = set()
    for i in range(root+1):
        if base[i] > 0:
            for j in range(i+1):
                tmp = base[::]
                tmp[i] -= 1
                for k in range(j,i):
                    tmp[k] += 1
                tmp = tuple(tmp)
                mex.add(calc(tmp))
    
    res = 0
    while res in mex:
        res += 1
    d[x] = res
    return res

top = [0] * (root+1)
top[-1] = 1
top = tuple(top)
calc(top)

for k,v in d.items():
    # even = sum(k[::2])
    # odd = sum(k[1::2])
    # if even % 2 == 0 and odd % 2 == 0 and v != 0:
    #     print(k,v)
    # elif not (even % 2 == 0 and odd % 2 == 0) and v == 0:
    #     print(k,v)
    # mod1 = sum(k[1::4])
    # mod3 = sum(k[3::4])
    # if mod1 % 2 == 1 and mod3 % 2 == 1 and v == 0:
    #     print(k,v)
    if sum(k) == 1:
        print(k,v)
