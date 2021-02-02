# a,b = map(int,input().split())
# a = list(map(int,input().split()))
# a = [list(map(int,input().split())) for _ in range(n)]

# import sys
# read = sys.stdin.buffer.read
# readline = sys.stdin.buffer.readline
# readlines = sys.stdin.buffer.readlines

# 検討?分　実装分 バグとり分

import sys
import os
f = open('../../input.txt', 'r')
sys.stdin = f

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

    def max_right(self, l: int, f):
        assert (0 <= l) & (l <= self.__n)
        assert f(self.__e())
        if(l == self.__n):
            return self.__n
        l += self.__size
        sm = self.__e()
        while(True):
            while(l % 2 == 0):
                l //= 2
            if(not f(self.__op(sm, self.__d[l]))):
                while(l < self.__size):
                    l *= 2
                    if(f(self.__op(sm, self.__d[l]))):
                        sm = self.__op(sm, self.__d[l])
                        l += 1
                return l - self.__size
            sm = self.__op(sm, self.__d[l])
            l += 1
            if(l & -l) == l:
                break
        return self.__n

    def min_left(self, r: int, f):
        assert (0 <= r) & (r <= self.__n)
        assert f(self.__e())
        if(r == 0):
            return 0
        r += self.__size
        sm = self.__e()
        while(True):
            r -= 1
            while(r > 1) & (r % 2):
                r //= 2
            if(not f(self.__op(self.__d[r], sm))):
                while(r < self.__size):
                    r = 2 * r + 1
                    if(f(self.__op(self.__d[r], sm))):
                        sm = self.__op(self.__d[r], sm)
                        r -= 1
                return r + 1 - self.__size
            sm = self.__op(self.__d[r], sm)
            if(r & -r) == r:
                break
        return 0


import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

n,k,*a = list(map(int,read().split()))

def op(x,y):
    x0,x1 = divmod(x,1<<20)
    y0,y1 = divmod(y,1<<20)
    if(x0 >= y0):
        return x
    else:
        return y

st = SegTree(op=max, e=lambda :0, v = list(range(300001)))
bef = [-1] * n
max_num = 0
last = -1
for i,ai in enumerate(a):
    l = max(0,ai-k)
    r = min(300000, ai+k)
    b0,b1 = divmod(st.prod(l,r+1),1<<20)
    if(b0 != 0):
        bef[i] = b1
    st.set(ai, ((b0+1)<<20) + i)
    if(max_num < b0+1):
        max_num = b0+1
        last = i

print(max_num)

# ans = [a[last]]
# while(bef[last] != -1):
#     last = bef[last]
#     ans.append(a[last])
#
# ans = ans[::-1]
