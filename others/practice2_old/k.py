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

import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

n,q = map(int,readline().split())
a = list(map(int,readline().split()))
query = list(map(int,read().split()))
MOD = 998244353


def op(x, y):
    x0, x1 = divmod(x, 1 << 32)
    y0, y1 = divmod(y, 1 << 32)
    return (((x0 + y0) % MOD) << 32) + x1 + y1


def mapping(f, x):
    x0, x1 = divmod(x, 1 << 32)
    f0, f1 = divmod(f, 1 << 32)
    return (((x0*f0+f1*x1) % MOD) << 32) + x1


def composition(f, g):
    # (ax+b)*c+d = acx + (bc+d)
    # f=[c,d] g=[a,b]
    f0, f1 = divmod(f, 1 << 32)
    g0, g1 = divmod(g, 1 << 32)
    res0 = g0*f0 % MOD
    res1 = (g1*f0+f1) % MOD
    return (res0 << 32) + res1


v = [(ai << 32)+1 for ai in a]
lst = LazySegTree(op=op,
                  e=lambda: 1,  # [value, size]
                  mapping=mapping,
                  composition=composition,
                  id=lambda: 1 << 32,  # [b,c]: ai*b+c
                  v=v
                  )

ans = []
i = 0
for _ in range(q):
    if(query[i] == 0):
        l, r, b, c = query[i+1:i+5]
        lst.apply_lr(l, r, (b << 32) + c)
        i += 5
    else:
        l,r = query[i+1:i+3]
        ans.append(lst.prod(l, r) >> 32)
        i += 3

print('\n'.join(map(str,ans)))
