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

class SegTree:
    """
    セグメントツリー
    https://atcoder.github.io/ac-library/production/document_ja/segtree.html

    Parameters
    ----------
    モノイドの型をSとする。

    op : function(S, S) -> S
        S × S を計算する関数。二分木の二つの子から親を求める際に使う。
    e : function() -> S
        モノイドの初期値を返す関数。単位元。
    n : int
        セグメントツリーで管理する要素数。n>=0を満たす。
        vが与えられない場合に参照する。要素は全てe()で初期化される。
    v : list[S]
        セグメントツリーで管理する要素の初期値
        vが与えられた場合nは無視する

    Attributes
    ----------
    _n : int
        セグメントツリーで管理する要素数
    _log : int
        _n <= 2**x を満たす最小のx
    _size : int
        1 << self._log
        セグメントツリー全体のサイズ
    _d : list[S]
        セグメントツリーで管理するモノイドを並べたリスト
        _d[1]が根に当たり、_d[x]の子は_d[x*2]と_d[x*2+1]になる。
    _lz : list[S]
        セグメントツリーで管理する遅延要素（写像）を並べたリスト
        _lz[1]が根に当たり、_lz[x]の子は_lz[x*2]と_lz[x*2+1]になる。
        サイズが_dの半分（セグメントツリーの葉には対応する遅延要素はないため。）
    _op : function(S, S)
    _e : function()
    _mapping : function(F, S)
    _composition : function(F, F)
    _id : function()
        それぞれParametersを参照

    Methods
    -------
    __init__(self, op, e, n=None, v=None)
        初期化
    _update(self, k)
        子の情報から親(=_d[k])を更新する

        Parameters
        ----------
        k : int
            更新箇所
    set(self, p, x)
        p番目の要素をxで置き換える
        その際、関連する値の更新を行う。
        Parameters
        ----------
        p : int
            0 <= p < self._n
            置き換える要素の番号。
        x : S
    get(self, p)
        p番目の要素の取得
        Parameters
        ----------
        p : int
            0 <= p < self._n
            置き換える要素の番号。
        Returns
        -------
        S
            self._d[p]
    prod(self, left, right)
        l番目～r-1番目の要素の演算結果
        Parameters
        ----------
        left : int
        right : int
            0 <= left <= right < self._n
        Returns
        -------
        S
            l番目～r-1番目の要素の演算結果
            l==rの場合はe()を返却する。
    all_prod(self)
        0番目～n-1番目の要素の演算結果
        Returns
        -------
        S
            0番目～n-1番目の要素の演算結果
    max_right(self, left, f)
        セグメントツリー上での二分探索結果を返却します。
        leftから始めて、右側に探索していく場合です。
        ※詳細は公式ドキュメント参照
        Parameters
        ----------
        left : int
            0 <= left <= self._n
            左側探索基準点
        f : function(S) -> bool
            f(e()) == Trueを満たす
        Returns
        -------
        int
            fが単調だとすれば、
            f(op(a[l], a[l + 1], ..., a[r - 1])) = true となる最大のr
    min_left(self, right, f)
        セグメントツリー上での二分探索結果を返却します。
        rightから始めて、左側に探索していく場合です。
        ※詳細は公式ドキュメント参照
        Parameters
        ----------
        right : int
            0 <= right <= self._n
            右側探索基準点
        f : function(S) -> bool
            f(e()) == Trueを満たす
        Returns
        -------
        int
            fが単調だとすれば、
            f(op(a[l], a[l + 1], ..., a[r - 1])) = true となる最小のl
    """
    def __init__(self, op, e, n=None, v=None):
        if n is None and v is None:
            v = []
        elif n is None:
            assert len(v) >= 0
        elif v is None:
            assert n >= 0
            v = [e()] * n
        self._n = len(v)
        self._log = (self._n - 1).bit_length()
        self._size = 1 << self._log
        self._d = [e()] * (2 * self._size)
        self._op = op
        self._e = e
        for i in range(self._n):
            self._d[self._size + i] = v[i]
        for i in range(self._size - 1, 0, -1):
            self._update(i)

    def _update(self, k):
        self._d[k] = self._op(self._d[2 * k], self._d[2 * k + 1])

    def set(self, p, x):
        assert 0 <= p and p < self._n
        p += self._size
        self._d[p] = x
        for i in range(1, self._log + 1):
            self._update(p >> i)

    def get(self, p):
        assert 0 <= p and p < self._n
        return self._d[p + self._size]

    def prod(self, left, right):
        assert 0 <= left <= right <= self._n
        sml = self._e()
        smr = self._e()
        left += self._size
        right += self._size

        while(left < right):
            if left & 1:
                sml = self._op(sml, self._d[left])
                left += 1
            if right & 1:
                right -= 1
                smr = self._op(self._d[right], smr)
            left //= 2
            right //= 2

        return self._op(sml, smr)

    def all_prod(self):
        return self._d[1]

import sys
read = sys.stdin.buffer.read

n,*data = map(int,read().split())
p = [x-1 for x in data[:n]]
it = iter(data[n:])
abc = [[a,b,c] for a,b,c in zip(it,it,it)]

inf = 10**15

cs_ab = [0] * (n+1)
cs_ac = [0] * (n+1)
cs_a_ = [0] * (n+1)
for i in range(n):
    cs_ab[i] = cs_ab[i-1] + min(abc[i][0], abc[i][1])

for i in range(n-1,-1,-1):
    cs_a_[i] = cs_a_[i+1] + abc[i][0]
    cs_ac[i] = cs_ac[i+1] + min(abc[i][0], abc[i][2])

def e():
    return inf

st = SegTree(op=min, e=e, n=n)
ans = inf
for pi in p:
    left = st.prod(0, pi) - cs_a_[pi]
    left = min(left, cs_ab[pi-1])
    ans = min(ans, left + cs_ac[pi+1])
    st.set(pi, left+cs_a_[pi+1])
print(ans)






# for i in range(n):
#     if p[i] != i:
#         break
# else:
#     print(0)
#     exit()

# hq = []
# base = (1<<20) - 1
# for i in range(n):
#     heappush(hq, (abc[i][0] << 20) + i)

# l = 0
# heappush(hq, (abc[p[l]][1] << 20) + p[l])
# r = n-1
# heappush(hq, (abc[p[r]][2] << 20) + p[r])

# done = [0] * n
# order = []
# while hq:
#     x = heappop(hq)
#     cost = x >> 20
#     i = x & base
#     if done[i] == 1:
#         continue
#     order.append(i)
#     done[i] = 1
#     flag = False
#     while l < n:
#         if done[p[l]] == 0:
#             if flag:
#                 heappush(hq, (abc[p[l]][1] << 20) + p[l])
#             break
#         l += 1
#         flag = True
#     flag = False
#     while r >= 0:
#         if done[p[r]] == 0:
#             if flag:
#                 heappush(hq, (abc[p[r]][2] << 20) + p[r])
#             break
#         r -= 1
#         flag = True
#     if l == n:
#         break

# idx = [0] * n
# for i,pi in enumerate(p):
#     idx[pi] = i

# def check(x):
#     q = p[::]
#     for i in order[:x]:
#         q[idx[i]] = -1
    
#     bef = -1
#     for i in range(n):
#         if q[i] == -1:
#             continue
#         if bef > q[i]:
#             return False
#         bef = q[i]
#     return True


# ng = 0
# ok = n-1
# while ok-ng > 1:
#     mid = (ok+ng)//2
#     if check(mid):
#         ok = mid
#     else:
#         ng = mid

# ans = 10 ** 15
# l = 0
# r = n-1
# now = 0
# done = [0] * n
# for i in range(n-1):
#     num = order[i]
#     done[num] = 1
#     now += abc[num][0]
#     while l < n:
#         if done[l] == 0:
#             break
#         if abc[l][0] > abc[l][1]:
#             now += abc[l][1] - abc[l][0]
#         l += 1
#     while r >= 0:
#         if done[r] == 0:
#             break
#         if abc[r][0] > abc[r][2]:
#             now += abc[r][2] - abc[r][0]
#         r -= 1
#     if i+1 >= ok:
#         ans = min(ans,now)
#         print(ok,i,ans)
# print(ans)

# print(order)    







# print(p)
# print(abc)