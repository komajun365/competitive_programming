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
    """
    長さ N の配列に対し、
    ・要素の 1 点変更
    ・区間の要素の総和
    を O(logN) で求めることが出来るデータ構造です。
    https://atcoder.github.io/ac-library/master/document_ja/fenwicktree.html

    本家は要素の型でmodintを指定することができるが、本実装はintに限る。
    (floatでも動くと思われるが、保証はしない)

    Parameters
    ----------
    n : int
        配列の長さ

    Attributes
    ----------
    _n : 配列の長さ
    _data : 管理する配列

    Methods
    -------
    __init__(self, n=0)
        初期化
    add(self, p, x)
        p番目の要素にxを加算する
        Parameters
        ----------
        p : int
             0 <= p < self._n
             加算する要素の番号
        x : int
            加算する値
    sum(self, left, right)
        _data[left] + _data[left+1] + .. + _data[right-1]を計算する
        Parameters
        ----------
        left : int
        right : int
    _sum(self, right)
        _data[0] + _data[1] + .. + _data[right-1]を計算する
        Parameters
        ----------
        right : int
    """
    def __init__(self, n=0):
        assert n >= 0
        self._n = n
        self._data = [0] * self._n

    def add(self, p, x):
        assert 0 <= p < self._n
        p += 1
        while p <= self._n:
            self._data[p - 1] += x
            p += p & -p

    def sum(self, left, right):
        assert 0 <= left <= right <= self._n
        return self._sum(right) - self._sum(left)

    def _sum(self, right):
        s = 0
        while right > 0:
            s += self._data[right - 1]
            right -= right & -right
        return s

n = int(input())
a = list(map(int,input().split()))
mod = 998244353

idx = [[] for _ in range(n+1)]
for i in range(n):
    ai = a[i]
    idx[ai].append(i)
for i in range(n+1):
    idx[i].append(n)

dp = FenwickTree(n+1)
dp.add(n, 1)

for i in range(n-1, -1, -1):
    ai = a[i]
    r = idx[ai].pop()
    dp.add(i, dp.sum(i, r+1) % mod)
    if r != n:
        dp.add(r, dp.sum(r,r+1) * -1)
    # print(dp._data)

ans = 0
for i in range(1,n+1):
    x = idx[i][-1] 
    if x == n:
        continue
    ans += dp.sum(x,x+1)
    ans %= mod
print(ans)

# print(dp._data)
# print


# n = int(input())
# a = list(map(int,input().split()))
# mod = 998244353

# idx = [[] for _ in range(n+1)]
# cnt = [0] * (n+1)
# for i in range(n):
#     ai = a[i]
#     idx[ai].append(i)
# for i in range(n+1):
#     idx[i].append(n)

# # cs = [0] * (n+2)
# # cs[n] = 1
# cnt = [0] * (n+1)
# tot = 0
# dp = [0] * (n+1)
# dp[n] = 1

# for i in range(n-1, -1, -1):
#     ai = a[i]
#     r = idx[ai].pop()
#     if r == n:
#         dp[i] = (tot + 1) % mod
#         tot = (tot + dp[i]) % mod
#         cnt[ai] = dp[i]
#     else:
#         dp[i] = tot
#         tot = (tot + dp[i] - cnt[ai]) % mod
#         cnt[ai] = dp[i]
#     print(dp)
#     print(cnt)
#     print(i,ai,r,tot)

#     # dp[i] = (cs[i+1] - cs[r+1]) % mod
#     # cs[i] = (cs[i+1] + dp[i]) % mod

# ans = 0
# for i in range(1,n+1):
#     if idx[i][-1] == n:
#         continue
#     ans += dp[idx[i][-1]]
#     ans %= mod
# print(ans)

# print(dp)
# # print(cs)
