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
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

n,m,*data = map(int,read().split())
a = data[:n]
it = iter(data[n:])
lrc = [[l,r,c] for l,r,c in zip(it,it,it)]
lrc.sort(key = lambda x: x[1])

cumsum = [0] * (n+1)
for i in range(n):
    cumsum[i+1] = cumsum[i] + a[i]

v = [-1 * i for i in cumsum]
st1 = SegTree(op=max,
             e= lambda:-1*10**18,
             v = [0]*(n+1))

st2 = SegTree(op=max,
             e= lambda:-1*10**18,
             v = v)


for l,r,c in lrc:
    now = st1.get(r)
    cand1 = st1.prod(0,l) + cumsum[r] - cumsum[l-1] - c
    cand2 = st2.prod(l,r) + cumsum[r] - c
    cand = max(cand1,cand2)
    if(now < cand):
        st1.set(r,cand)
        st2.set(r,cand-cumsum[r])

print(st1.all_prod())


'''
edpcのあれでは？
'''