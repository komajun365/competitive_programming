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

    def max_right(self, l: int, g):
        assert (0 <= l) & (l <= self.__n)
        assert g(self.__e())
        if(l == self.__n):
            return self.__n
        l += self.__size
        for i in range(self.__log, 0, -1):
            self.__push(l >> i)
        sm = self.__e()
        while(True):
            while(l % 2 == 0):
                l //= 2
            if(not g(self.__op(sm, self.__d[l]))):
                while(l < self.__size):
                    self.__push(l)
                    l *= 2
                    if(g(self.__op(sm, self.__d[l]))):
                        sm = self.__op(sm, self.__d[l])
                        l += 1
                return l - self.__size
            sm = self.__op(sm, self.__d[l])
            l += 1
            if(l & -l) == l:
                break
        return self.__n

    def min_left(self, r: int, g):
        assert (0 <= r) & (r <= self.__n)
        assert g(self.__e())
        if(r == 0):
            return 0
        r += self.__size
        for i in range(self.__log, 0, -1):
            self.__push((r-1) >> i)
        sm = self.__e()
        while(True):
            r -= 1
            while(r > 1) & (r % 2):
                r //= 2
            if(not g(self.__op(self.__d[r], sm))):
                while(r < self.__size):
                    self.__push(r)
                    r = 2 * r + 1
                    if(g(self.__op(self.__d[r], sm))):
                        sm = self.__op(self.__d[r], sm)
                        r -= 1
                return r + 1 - self.__size
            sm = self.__op(self.__d[r], sm)
            if(r & -r) == r:
                break
        return 0

    def all_push(self):
        for i in range(1,self.__size):
            self.__push(i)

    def get_all(self):
        self.all_push()
        return self.__d[self.__size:self.__size+self.__n]

    def print(self):
        print(list(map(lambda x: divmod(x,(1<<30)),self.__d)))
        print(self.__lz)
        print('------------------')


import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

n,q,*query = map(int,read().split())
MOD = 998244353

mod_10 = [1] * (n+1)
mod_11 = [0] * (n+1)
for i in range(1,n+1):
    mod_10[i] = (mod_10[i-1] *10)% MOD
    mod_11[i] = (mod_11[i-1] *10 + 1)% MOD

def op(x,y):
    x0,x1 = divmod(x,1<<30) # [size, mod]
    y0,y1 = divmod(y,1<<30)
    if(x==0):
        return y
    if(y==0):
        return x
    res0 = x0 + y0
    res1 = (x1 * mod_10[y0] + y1)% MOD
    return (res0<<30) + res1

def mapping(f,x):
    if(f==-1):
        return x
    x0,x1 = divmod(x,1<<30)
    res1 = (mod_11[x0] * f)%MOD
    return (x0<<30) + res1

def composition(f,g):
    if(f==-1):
        return g
    return f

v = [(1<<30) + 1]*n
lst = LazySegTree(op=op,
                  e=lambda: 0,
                  mapping=mapping,
                  composition=composition,
                  id=lambda: -1,
                  v=v
                  )


ans = []
it = iter(query)
for l,r,d in zip(it,it,it):
    # lst.print()
    lst.apply_lr(l-1,r,d)
    tmp = lst.all_prod()
    ans.append(tmp % (1<<30))

print('\n'.join(map(str,ans)))
# lst.print()

# print(mod_10[:10])
# print(mod_11[:10])
# print(query)
