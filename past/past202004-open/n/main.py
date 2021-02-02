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

import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
import bisect

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
    
    def add(self, p: int, x):
        assert (0 <= p) & (p < self.__n)
        p += self.__size
        self.__d[p] += x
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

    def pr(self):
        print(self.__d)

n,q,*data = map(int,read().split())
xydc = data[:n*4]
ab = data[n*4:]
ans = [0] * q

xs = set()
ys = set()
it = iter(xydc)
for x,y,d,c in zip(it,it,it,it):
    xs.add(x)
    xs.add(x+d+1)
    ys.add(y)
    ys.add(y+d+1)

xs = list(xs)
xs.sort()
ys = list(ys)
ys.sort()

encode_x = dict()
for i,xi in enumerate(xs):
    encode_x[xi] = i

encode_y = dict()
for i,yi in enumerate(ys):
    encode_y[yi] = i

it = iter(xydc)
query = []
for x,y,d,c in zip(it,it,it,it):
    query.append([encode_y[y],encode_x[x],encode_x[x+d+1],c])
    query.append([encode_y[y+d+1],encode_x[x],encode_x[x+d+1],-c])
query.sort()

query_ab = []
for i in range(q):
    a,b = ab[i*2:i*2+2]
    a = bisect.bisect_left(xs,a+1)-1
    b = bisect.bisect_left(ys,b+1)-1
    query_ab.append([b,a,i])
query_ab.sort()

def op(x,y):
    return x+y

def e():
    return 0

st = SegTree(op=op, e=e, n=len(xs)+1)
qi = 0
for b,a,i in query_ab:

    while(qi < len(query)):
        if query[qi][0] > b:
            break
        _,xl,xr,c = query[qi]
        st.add(xl,c)
        st.add(xr,-c)
        qi += 1
    
    if(b == -1) or (a== -1):
        ans[i] = 0
        continue
    
    ans[i] = st.prod(0,a+1)

print('\n'.join(map(str,ans)))
# print(query)
# print(query_ab)
# print(xs)
# print(ys)