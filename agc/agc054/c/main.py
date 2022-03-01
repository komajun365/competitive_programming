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

n,k = map(int,input().split())
p = list(map(int,input().split()))
mod = 998244353

ft = FenwickTree(n+1)
cnt = []
for pi in p:
    cnt.append(ft.sum(pi,n+1))
    ft.add(pi,1)

ans = 1
for i in range(n-1,-1,-1):
    if cnt[i] == k:
        j = i+1
        while j < n:
            if p[j] > p[i]:
                j += 1
            else:
                break
        ans *= (j-i)
        ans %= mod
print(ans)
    
