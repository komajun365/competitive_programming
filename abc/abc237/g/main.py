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

'''
lazysegtree
引数
・op : 二項演算関数
　　　　区間最大：max、区間和：sum など
・e　：opにおける単位元を生成する関数
・mapping　：遅延していたものを要素に反映させる関数
・composition　：遅延操作を追加する関数
・id　：mappingにおける恒等写像

・n　：配列の長さ（vを指定しない場合、長さN、値e()の配列を初期値とする）
・v　：初期値配列

（参考）
https://betrue12.hateblo.jp/entry/2020/09/22/194541

def op(x, y):
    return xxx

def mapping(f, x):
    return xxx

def composition(f, g):
    return xxx
    
lst = LazySegTree(op=op,
                  e=lambda: 0,
                  mapping=mapping,
                  composition=composition,
                  id=lambda: 0,
                  v=v
                  )

'''

# rangesum & valueの0or1を遅延更新
class LazySegTree:
    def __init__(self, v: list = []):
        assert (len(v) > 0) | (n > 0)
        self.__n = len(v)
        self.__log = (self.__n - 1).bit_length()
        self.__size = 1 << self.__log
        self.__d = [0] * (2 * self.__size)
        self.__lz = [-1] * self.__size
        self.__op = lambda x,y : x+y
        self.__e = lambda : 0
        # self.__mapping = mapping
        # self.__composition = composition
        self.__id = lambda : -1

        for i in range(self.__n):
            self.__d[self.__size + i] = v[i]
        for i in range(self.__size - 1, 0, -1):
            self.__update(i)

    def __update(self, k: int):
        self.__d[k] = self.__op(self.__d[2 * k], self.__d[2 * k + 1])

    def __all_apply(self, k: int, f):
        # self.__d[k] = self.__mapping(f, self.__d[k])
        if f == -1:
            return
        elif f == 0:
            self.__d[k] = 0
        elif f == 1:
            self.__d[k] = 2**(self.__log - (k).bit_length() + 1)
        if(k < self.__size):
            self.__lz[k] = f

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
        # self.__d[p] = self.__mapping(f, self.__d[p])
        if f != -1:
            self.__d[p] = f
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


    
    def print(self):
        print(self.__d)
        print(self.__lz)

import sys
read = sys.stdin.buffer.read

n,q,x,*data = map(int,read().split())
p = data[:n]
clr = data[n:]

ans = 0
p2 = []
for i,pi in enumerate(p):
    if pi == x:
        p2.append(0)
        ans = i
    elif pi < x:
        p2.append(0)
    else:
        p2.append(1)

lst = LazySegTree(v=p2)

it = iter(clr)
for ci,li,ri in zip(it,it,it):
    li -= 1
    plus = lst.prod(li, ri)
    minus = ri-li-plus
    if ci == 1:
        if li <= ans < ri:
            minus -= 1
            ans = li + minus
            lst.set(ans, 0)
        lst.apply_lr(li, li+minus, 0)
        lst.apply_lr(ri-plus, ri, 1)
    else:
        if li <= ans < ri:
            minus -= 1
            ans = li + plus
            lst.set(ans, 0)
        lst.apply_lr(li, li+plus, 1)
        lst.apply_lr(ri-minus, ri, 0)

print(ans+1)