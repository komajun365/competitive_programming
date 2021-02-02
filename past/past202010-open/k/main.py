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
read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines

class FenwickTree:
    def __init__(self, n: int, mod: int = 0):
        self.__mod = mod
        self.__n = n
        self.__data = [0] * self.__n

    def add(self, p: int, x: int):
        assert (0 <= p) & (p < self.__n)
        if(self.__mod == 0):
            self.__add_mod0(p, x)
        else:
            self.__add_mod(p, x)

    def __add_mod0(self, p: int, x: int):
        p += 1
        while(p <= self.__n):
            self.__data[p - 1] += x
            p += p & -p

    def __add_mod(self, p: int, x: int):
        p += 1
        while(p <= self.__n):
            self.__data[p - 1] += x
            self.__data[p - 1] %= self.__mod
            p += p & -p

    def sum(self, l: int, r: int):
        assert (0 <= l) & (l <= r) & (r <= self.__n)
        if(self.__mod == 0):
            return self.__sum_mod0(r) - self.__sum_mod0(l)
        else:
            return (self.__sum_mod(r) - self.__sum_mod(l)) % self.__mod

    def __sum_mod0(self, r: int):
        s = 0
        while(r > 0):
            s += self.__data[r - 1]
            r -= r & -r
        return s

    def __sum_mod(self, r: int):
        s = 0
        while(r > 0):
            s += self.__data[r - 1]
            s %= self.__mod
            r -= r & -r
        return s

k,*data = map(int,read().split())
mod = 10**9

n = []
a = []
idx = 0
for _ in range(k):
    ni = data[idx]
    a.append(data[idx+1:idx+ni+1])
    idx += ni+1

q = data[idx]
b = data[idx+1:]

cnt = []
inv = []
def get_info(ai):
    cnt_i = [0] * 21
    inv_i = 0

    BIT = FenwickTree(21)
    for i,x in enumerate(ai):
        cnt_i[x] += 1
        BIT.add(x,1)
        inv_i += i + 1 - BIT.sum(0,x+1)
    inv_i %= mod
    
    return cnt_i,inv_i

for ai in a:
    # print(ai)
    cnt_i,inv_i = get_info(ai)
    # print(cnt_i)
    # print(inv_i)
    cnt.append(cnt_i)
    inv.append(inv_i)

ans = 0
cnt_x = [0] * 21
for bi in b:
    bi -= 1
    ans += inv[bi]
    cs = 0
    for j in range(2,21):
        cs += cnt[bi][j-1]
        ans += cnt_x[j] * cs
    ans %= mod

    for j in range(1,21):
        cnt_x[j] += cnt[bi][j]

print(ans)











'''
aiの転倒数と、各要素数のカウントをしておく

末尾にyを追加する際
・転倒数をaddする
・xの２の数＊yの１の数　+　ｘの３の数＊ｙの2以下の数　+　。。。をadd
をすれば良い




'''