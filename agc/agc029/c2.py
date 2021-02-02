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

class LazySegTree:
    def __init__(self, op, e, mapping, composition, id,
                 n: int = -1, v: list = []):
        assert (len(v) > 0) | (n > 0)
        if(len(v) == 0):
            v = [e()] * n
        self.__n = len(v)
        self.__log = (self.__n - 1).bit_length()
        self.__size = 1 << self.__log
        self.__d = [e()] * (2 * self.__size)
        self.__lz = [id()] * self.__size
        self.__op = op
        self.__e = e
        self.__mapping = mapping
        self.__composition = composition
        self.__id = id

        for i in range(self.__n):
            self.__d[self.__size + i] = v[i]
        for i in range(self.__size - 1, 0, -1):
            self.__update(i)

    def __update(self, k: int):
        self.__d[k] = self.__op(self.__d[2 * k], self.__d[2 * k + 1])

    def __all_apply(self, k: int, f):
        self.__d[k] = self.__mapping(f, self.__d[k])
        if(k < self.__size):
            self.__lz[k] = self.__composition(f, self.__lz[k])

    def __push(self, k: int):
        self.__all_apply(2*k, self.__lz[k])
        self.__all_apply(2*k+1, self.__lz[k])
        self.__lz[k] = self.__id()

    def set(self, p: int, x):
        assert (0 <= p) & (p < self.__n)
        p += self.__size
        for i in range(self.__log, 0, -1):
            self.__push(p >> i)
        self.__d[p] = x
        for i in range(1, self.__log + 1):
            self.__update(p >> i)

    def get(self, p: int):
        assert (0 <= p) & (p < self.__n)
        p += self.__size
        for i in range(self.__log, 0, -1):
            self.__push(p >> i)
        return self.__d[p]

    def prod(self, l: int, r: int):
        assert (0 <= l) & (l <= r) & (r <= self.__n)
        if(l == r):
            return self.__e()

        l += self.__size
        r += self.__size

        for i in range(self.__log, 0, -1):
            if((l >> i) << i) != l:
                self.__push(l >> i)
            if((r >> i) << i) != r:
                self.__push(r >> i)

        sml = self.__e()
        smr = self.__e()
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

    def apply(self, p: int, f):
        assert (0 <= p) & (p < self.__n)
        p += self.__size
        for i in range(self.__log, 0, -1):
            self.__push(p >> i)
        self.__d[p] = self.__mapping(f, self.__d[p])
        for i in range(1, self.__log+1):
            self.__update(p >> i)

    def apply_lr(self, l: int, r: int, f):
        assert (0 <= l) & (l <= r) & (r <= self.__n)
        if(l == r):
            return

        l += self.__size
        r += self.__size

        for i in range(self.__log, 0, -1):
            if((l >> i) << i) != l:
                self.__push(l >> i)
            if((r >> i) << i) != r:
                self.__push((r-1) >> i)

        l2, r2 = l, r
        while(l < r):
            if(l & 1):
                self.__all_apply(l, f)
                l += 1
            if(r & 1):
                r -= 1
                self.__all_apply(r, f)
            l //= 2
            r //= 2
        l, r = l2, r2

        for i in range(1, self.__log+1):
            if((l >> i) << i) != l:
                self.__update(l >> i)
            if((r >> i) << i) != r:
                self.__update((r-1) >> i)


n = int(input())
a = list(map(int,input().split()))

a_val = set(a)
a_val.add(1)
a_val = list(a_val)
a_val.sort()
encode = dict()
for i,ai in enumerate(a_val):
    encode[ai] = i
a_val_dif = [0] * len(a_val)
for i in range(1,len(a_val)):
    a_val_dif[i] = a_val[i] - a_val[i-1]
b = []
for ai in a:
    b.append(encode[ai])

def mapping(f, x):
    if(f==-1):
        return x
    return f

def composition(f, g):
    if(f==-1):
        return g
    return f

def check(mid):
    if(mid==1):
        for i in range(n):
            if(a[i] >= a[i+1]):
                return False
        return True

    x = mid
    ex_lim = 1
    while(x < n):
        ex_lim += 1
        x *= mid

    v = [1] * (b[0]+1)  + [0]*(len(a_val) - b[0] - 1)
    lst = LazySegTree(op = max, e=lambda:0,
                     mapping=mapping, composition=composition,id=lambda:-1,
                     v=v)
    bef = b[0]
    for i,bi in enumerate(b[1:],1):
        if(bef > bi):
            lst.apply_lr(bi+1,bef+1,0)
        elif(bef < bi):
            lst.apply_lr(bef+1,bi,1)
        ind = bi
        while(ind >= 0):
            if(ind==0):
                new = lst.get(ind) + 1
                lst.set(ind, new)
                break
            new = lst.get(ind) + 1
            if(a_val_dif[ind] >= ex_lim):
                lst.set(ind, new)
                break
            if( new <= mid**a_val_dif[ind]):
                lst.set(ind, new)
                break
            lst.set(ind, 1)
            ind -= 1
        bef = bi
    if( lst.get(0) <= mid):
        return True
    else:
        return False


ok = n
ng = 0
while(ok-ng>1):
    mid = (ok+ng)//2
    if( check(mid) ):
        ok = mid
    else:
        ng = mid
print(ok)
