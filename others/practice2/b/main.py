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

import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
 
n,q = map(int,readline().split())
a = list(map(int,readline().split()))
query = list(map(int,read().split()))
 
ft = FenwickTree(n)
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