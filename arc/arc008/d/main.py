# oj t -c "python main.py" -d "./tests/" 

# a,b = map(int,input().split())
# a = list(map(int,input().split()))
# a = [list(map(int,input().split())) for _ in range(n)]

# import sys
# read = sys.stdin.buffer.read
# readline = sys.stdin.buffer.readline
# readlines = sys.stdin.buffer.readlines

# 検討?分　実装分 バグとり分

# import sys
# import os
# f = open('../../../input.txt', 'r')
# sys.stdin = f

class SegTree:
    def __init__(self, op, e, n: int = -1, v: list = []):
        assert (len(v) > 0) | (n > 0)
        if(len(v) == 0):
            v = [e()] * n
        self.__n = len(v)
        self.__log = (self.__n - 1).bit_length()
        self.__size = 1 << self.__log
        self.__d = [e()] * (2 * self.__size)
        self.__op = op
        self.__e = e
        for i in range(self.__n):
            self.__d[self.__size + i] = v[i]
        for i in range(self.__size - 1, 0, -1):
            self.__update(i)

    def __update(self, k: int):
        self.__d[k] = self.__op(self.__d[2 * k], self.__d[2 * k + 1])

    def set(self, p: int, x):
        assert (0 <= p) & (p < self.__n)
        p += self.__size
        self.__d[p] = x
        for i in range(1, self.__log + 1):
            self.__update(p >> i)

    def get(self, p: int):
        assert (0 <= p) & (p < self.__n)
        return self.__d[p + self.__size]

    def prod(self, l: int, r: int):
        assert (0 <= l) & (l <= r) & (r <= self.__n)
        sml = self.__e()
        smr = self.__e()
        l += self.__size
        r += self.__size

        while(l < r):
            if(l & 1):
                sml = self.__op(sml, self.__d[l])
                l += 1
            if(r & 1):
                r -= 1
                smr = self.__op(self.__d[r], smr)
            l //= 2
            r //= 2

        return self.__op(sml, smr)

    def all_prod(self):
        return self.__d[1]

import sys
read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines

n,m = map(int,readline().split())
if(m==0):
    print(1)
    print(1)
    exit()
data = [list(si.split()) for si in readlines()]

def op(x,y):
    r0 = x[0] * y[0]
    r1 = x[1] * y[0] + y[1]
    return [r0,r1]

def e():
    return [1,0]

p = [int(s0)  for s0,_0,_1 in data]
ps = list(set(p))
ps.sort()
encode = dict()
for i,pi in enumerate(ps):
    encode[pi] = i

num = len(ps)
st = SegTree(op=op, e=e, n=num)

ans = [1]
for p,a,b in data:
    p = int(p)
    a = float(a)
    b = float(b)
    st.set(encode[p],[a,b] )
    ans.append( sum(st.all_prod()) )

print(min(ans))
print(max(ans))

