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

n = int(input())
a = list(map(int,input().split()))

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

# 計算量オーダーは n = len(a),m= max(a)としてO(nlogm)
def calc_invs(a):
    m = max(a)
    bit = FenwickTree(m+1)
    num = 0
    res = [0]
    for i,ai in enumerate(a):
        bit.add(ai,1)
        num += i + 1 - bit.sum(0,ai+1)
        res.append(num)
    return res

inv_l = calc_invs(a)
inv_r = calc_invs(a[::-1])
for i in range(n+1):
    inv_r[i] = (i * (i-1))//2 - inv_r[i]
inv_r = inv_r[::-1]


# print(inv_l)
# print(inv_r)

inv_sum = inv_l[-1]
ans = []
for i in range(n):
    tmp = inv_l[i] + inv_r[i]
    dif = inv_sum - tmp
    tmp += i * (n-i) - dif
    ans.append(tmp)

print('\n'.join(map(str,ans)))