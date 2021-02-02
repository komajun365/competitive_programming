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

    def get_all(self):
        return self.__d[self.__size : self.__size+self.__n]


def calc(n,a):

    # n = int(input())
    # a = [1] + list(map(int,input().split()))
    a = [1] + a

    a_il = [[i,ai] for i,ai in enumerate(a[1:],1)]
    a_il.sort(key=lambda x: -1*(x[1]*10**6 + x[0]))

    st = SegTree(op = max, e=lambda:0, n=n+1)
    ls = [0] * (n+1)
    for i,ai in a_il[::-1]:
        ls[i] = st.prod(0,i)
        st.set(i, i)

    def check(mid):
        if(mid==1):
            b = a[::]
            b.sort()
            for i in range(1,n):
                if(b[i] == b[i-1]):
                    return False
            return True

        cnt = [1]*(n+1)
        cnt[0] = 0
        for i,ai in a_il:
            l = ls[i]
            if(a[i] == a[l]):
                cnt[l] += cnt[i]
            else:
                x = a[i] - a[l]
                if(x > 20):
                    continue
                else:
                    cnt[l] += (cnt[i]-1) // (mid**x)
        return cnt[0] <= mid


    ok = n
    ng = 0
    while(ok-ng>1):
        mid = (ok+ng)//2
        if( check(mid) ):
            ok = mid
        else:
            ng = mid
    # print(ok)
    return ok

import random

for _ in range(1000):
    n = random.randint(5,100)
    a = [random.randint(1,10) for _ in range(n)]

    print(n)
    # print(a)
    print(calc(n,a))
