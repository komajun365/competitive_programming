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

    def print(self):
        print(list(map(lambda x: divmod(x,(1<<20)),self.__d)))
        print(self.__lz)
        print('------------------')

import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

h,w = map(int,readline().split())
ab = list(map(int,read().split()))

def op(x, y):
    # x0,x1 = cost,leftとする
    x0, x1 = divmod(x, (1<<20))
    y0, y1 = divmod(y, (1<<20))
    res0 = min(x0,y0)
    res1 = min(x1,y1)
    return (res0 << 20) + res1

def mapping(f, x):
    x0, x1 = divmod(x, (1<<20))
    if(f == (1<<20)-1):
        return x
    if(f==0):
        res0 = (1<<20)-1
    else:
        res0 = x1-f

    return (res0 << 20) + x1


def composition(f, g):
    return min(f,g)

def calc(h,w,ab):
    v = [ i for i in range(w+1)]
    v[0] = ((1<<20)-1)<<20
    lst = LazySegTree(op=op,
                      e=lambda: (1<<40) - 1,
                      mapping=mapping,
                      composition=composition,
                      id=lambda: (1<<20)-1,
                      v=v
                      )
    ans = []
    it = iter(ab)
    for a,b,i in zip(it,it, range(1,h+1)):
        l = a-1
        f = l - ((lst.get(l)) >> 20)
        lst.apply_lr(a,b+1, f)
        x = lst.all_prod()
        x0,x1 = divmod(x, (1<<20))
        if(x0 >= w):
            ans.append(-1)
        else:
            ans.append(x0+i)
        # lst.print()

    # print('\n'.join(map(str,ans)))
    return ans

def calc_s(h,w,ab):
    ans = []
    inf = 10**6
    dp = [0] * (w+1)
    dp[0] = inf
    it = iter(ab)
    for a,b,i in zip(it,it, range(1,h+1)):
        for j in range(a,b+1):
            dp[j] = max(dp[j], dp[a-1] + (j-a+1))
        tmp = min(dp)
        if(tmp >= inf):
            ans.append(-1)
        else:
            ans.append(tmp + i)
    return ans

import random
for _ in range(1000):
    h = random.randint(5,20)
    w = random.randint(5,20)
    ab = []
    for _ in range(h):
        l = random.randint(1,w)
        r = random.randint(1,w)
        ab.append(min(l,r))
        ab.append(max(l,r))

    ans = calc(h,w,ab)
    ans_s = calc_s(h,w,ab)
    if(ans != ans_s):
        print(h,w)
        print(ab)
        print(ans)
        print(ans_s)
        exit()

# h,w = 5,5
# ab = [5, 5, 3, 4, 2, 5, 1, 3, 2, 3]
#
# ans = calc(h,w,ab)
# print(ans)
# ans = calc_s(h,w,ab)
# print(ans)
