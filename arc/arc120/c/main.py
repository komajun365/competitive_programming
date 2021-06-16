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

from collections import deque

n = int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))

ad = dict()
for i in range(n):
    tmp = a[i] + i
    if not tmp in ad:
        ad[tmp] = deque()
        ad[tmp].append(i)
    else:
        ad[tmp].append(i)

ft = FenwickTree(n)
ans = 0
for i in range(n):
    tmp = b[i] + i
    # print(tmp,ad)
    if not tmp in ad:
        print(-1)
        exit()
    if len(ad[tmp]) == 0:
        print(-1)
        exit()
    
    idx = ad[tmp].popleft()
    ans += idx - ft.sum(0,idx)
    ft.add(idx, 1)
print(ans)



