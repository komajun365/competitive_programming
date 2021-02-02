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

s = input()
n = len(s)

idx = dict()
for i,si in enumerate(s):
    if si in idx:
        idx[si].append(i)
    else:
        idx[si] = [i]

odd = 0
for k,v in idx.items():
    if len(v) % 2 == 1:
        odd += 1

if odd > n % 2:
    print(-1)
    exit()

bit = FenwickTree(n)
use = [0] * n
left = 0
ans = 0
for i in range(n):
    if use[i] == 1:
        continue

    si = s[i]
    r = idx[si].pop()
    if i == r:
        ans += n//2 - left
        use[i] = 1
        continue
    
    ans += (n-1-left) - r + bit.sum(0,r)
    left += 1
    use[i] = 1
    use[r] = 1
    bit.add(r,1)

print(ans)

    
