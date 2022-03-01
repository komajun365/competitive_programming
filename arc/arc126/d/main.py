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

# 計算量オーダーは n = len(a),m= max(a)としてO(nlogm)
def calc_invs(a, m):
    # m = max(a)
    bit = FenwickTree(m+1)
    res = 0
    for i,ai in enumerate(a):
        bit.add(ai,1)
        res += i + 1 - bit.sum(0,ai+1)
    return res

import itertools

n,k = map(int,input().split())
a = list(map(lambda x: int(x)-1,input().split()))

left = []
right = []
for i in range(n):
    left.append([-1] * k)
    for j in range(i,-1,-1):
        if left[-1][a[j]] == -1:
            left[-1][a[j]] = j
    right.append([-1] * k)
    for j in range(i,n):
        if right[-1][a[j]] == -1:
            right[-1][a[j]] = j

def calc(x,ans):
    res = 0
    for i in range(k-1):
        res += (x[i+1] - x[i] - 1) * min(i+1, k-i-1)
    if res >= ans:
        return ans
    seq = []
    for xi in x:
        seq.append(a[xi])
    res += calc_invs(seq, k-1)
    return res

ans = n**3
for i in range(n):
    com = []
    for j in range(k):
        if a[i] != j:
            com.append(j)
    for c in itertools.combinations(com, (k-1)//2):
        x = [i] * k
        for ci in c:
            x[ci] = left[i][ci]
        
        for j in range(k):
            if x[j] == i:
                x[j] = right[i][j]
            if x[j] == -1:
                break
        else:
            x.sort()
            ans = min(ans, calc(x,ans))

print(ans)        
        
    # for bit in range(2**(k-1)):
    #     x = [idx[i]]
    #     for j in range(k-1):
    #         if (bit>>j) & 1:
    #             xj = left[i][j+1]
    #         else:
    #             xj = right[i][j+1]
    #         if xj == -1:
    #             break
    #         x.append(xj)
    #     else:
    #         x.sort()
    #         ans = min(ans, calc(x))
        # print(i,bit,x,ans)


# cnt = [0] * (k+1)
# for ai in a:
#     cnt[ai] += 1

# m = min(cnt[1:])
# for num in range(1,k+1):
#     if cnt[num] == m:
#         break

# idx = []
# for i in range(n):
#     a[i] = (a[i] - num) % k
#     if a[i] == 0:
#         idx.append(i)

# left = []
# right = []
# for i in idx:
#     left.append([-1] * k)
#     for j in range(i-1,-1,-1):
#         if left[-1][a[j]] == -1:
#             left[-1][a[j]] = j
#     right.append([-1] * k)
#     for j in range(i+1,n):
#         if right[-1][a[j]] == -1:
#             right[-1][a[j]] = j

# def calc(x):
#     res = 0
#     for i in range(k-1):
#         res += (x[i+1] - x[i] - 1) * min(i+1, k-i-1)
#     seq = []
#     for xi in x:
#         seq.append(a[xi])
#     res += calc_invs(seq, k-1)
#     return res

# ans = n**3
# l = len(idx)
# for i in range(l):
#     for bit in range(2**(k-1)):
#         x = [idx[i]]
#         for j in range(k-1):
#             if (bit>>j) & 1:
#                 xj = left[i][j+1]
#             else:
#                 xj = right[i][j+1]
#             if xj == -1:
#                 break
#             x.append(xj)
#         else:
#             x.sort()
#             ans = min(ans, calc(x))
#         # print(i,bit,x,ans)

# print(ans)
    



# # print(a)
# # print(left)
# # print(right)