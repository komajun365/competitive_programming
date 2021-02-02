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

class fenwick_tree():
    def __init__(self, n:int, mod:int = 0):
        self.__mod = mod
        self.__n = n
        self.__data = [0] * self.__n

    def add(self, p:int, x:int):
        assert (0 <= p) & (p < self.__n)
        if(self.__mod == 0):
            self.__add_mod0(p,x)
        else:
            self.__add_mod(p,x)

    def __add_mod0(self, p:int, x:int):
        p+=1
        while( p<= self.__n):
            self.__data[p-1] += x
            p += p & -p

    def __add_mod(self, p:int, x:int):
        p+=1
        while( p<= self.__n):
            self.__data[p-1] += x
            self.__data[p-1] %= self.__mod
            p += p & -p

    def sum(self, l:int, r:int):
        assert (0 <= l) & (l <= r) & (r <= self.__n)
        if(self.__mod == 0):
            return self.__sum_mod0(r) - self.__sum_mod0(l)
        else:
            return self.__sum_mod(r) - self.__sum_mod(l)

    def __sum_mod0(self, r:int):
        s = 0
        while(r > 0):
            s += self.__data[r-1]
            r -= r & -r
        return s

    def __sum_mod(self, r:int):
        s = 0
        while(r > 0):
            s += self.__data[r-1]
            s %= self.__mod
            r -= r & -r
        return s

import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

n,q = map(int,readline().split())
a = list(map(int,readline().split()))
query = list(map(int,read().split()))

ft = fenwick_tree(n,mod=10**18)
ans = []

for i,ai in enumerate(a):
    ft.add(i,ai)

i = 0
for _ in range(q):
    if(query[i]==0):
        p,x = query[i+1:i+3]
        ft.add(p,x)
    else:
        l,r = query[i+1:i+3]
        ans.append(ft.sum(l,r))
    i += 3

print('\n'.join(map(str,ans)))
