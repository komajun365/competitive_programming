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

def primitive_root(m):
    """
    整数mの最小原始根を計算する

    Parameters
    ----------
    m : int
        2以上の整数

    Returns
    -------
    int
        mの最小原始根
    """
    if m == 2:
        return 1
    if m == 167772161:
        return 3
    if m == 469762049:
        return 3
    if m == 754974721:
        return 11
    if m == 998244353:
        return 3

    divs = [2] + [0] * 19
    cnt = 1
    x = (m - 1) // 2
    while x % 2 == 0:
        x //= 2

    i = 3
    while i**2 <= x:
        if x % i == 0:
            divs[cnt] = i
            cnt += 1
            while x % i == 0:
                x //= i

        i += 2

    if x > 1:
        divs[cnt] = x
        cnt += 1

    g = 2
    while True:
        for i in range(cnt):
            if pow(g, (m-1)//divs[i], m) == 1:
                break

        else:
            return g

        g += 1

def ceil_pow2(n):
    """
    n <= 2**x を満たす最小のxを返却する。

    Parameters
    ----------
    n : int
        0以上の整数

    Returns
    -------
    int
        n <= 2**x を満たす最小のx

    """
    if n < 1:
        return 0
    return (n-1).bit_length()


def bsf(n):
    """
    自然数を2bitで表現したときに、右から見て最初に1が立つ桁が何桁目かを返却する。
    （0-indexed）

    Parameters
    ----------
    n : int
        1以上の整数

    Returns
    -------
    int
        2bitで表現したときに、右から見て最初に1が立つ桁（0-indexed）

    """
    return (n & -n).bit_length()-1


class Convolution:
    """
    畳み込みを行う。
    長さNの数列Aと長さMの数列Bから、長さ(N+M-1)の数列Cを計算する。
    c_i = sum_{j=0}^{i} a_j * b_{i-j}

    Parameters
    ----------
    mod : int
        畳み込みを計算する際の法

    Attributes
    ----------
    _first1 : bool
        butterfly関数を初めて呼び出したかどうかを表すbool値
    _first2 : bool
        butterfly_inv関数を初めて呼び出したかどうかを表すbool値
    _sum_e : list
    _sum_ie : list
        _sum_eの逆元のリスト
    _mod : int
        畳み込みを計算する際の法
    _root : int
        _modの最小原始根

    Methods
    -------
    __init__(self, mod)
        初期化
    _butterfly(self, a)
        バタフライ演算を実行する

        Parameters
        ----------
        a : array_like
            バタフライ演算を施す配列
    _butterfly_inv(self, a)
        バタフライ演算の逆演算を実行する

        Parameters
        ----------
        a : array_like
            バタフライ演算の逆演算を施す配列
    convolution(self, a, b)
        畳み込みを計算した結果の配列を返却する
        a, bのいずれかの配列が空の場合は空のリストを返却する

        Parameters
        ----------
        a, b : array_like
            畳み込みを計算する対象となる2つの配列

        Returns
        -------
        list
            配列a, bに対して畳み込みを計算した結果

    See Also
    --------
    https://github.com/atcoder/ac-library/blob/master/document_ja/convolution.md
    """
    def __init__(self, mod):
        self._first1 = True
        self._first2 = True
        self._sum_e = [0] * 30
        self._sum_ie = [0] * 30
        self._mod = mod
        self._root = primitive_root(mod)

    def _butterfly(self, a):
        n = len(a)
        h = ceil_pow2(n)
        if self._first1:
            self._first1 = False
            es = [0] * 30
            ies = [0] * 30
            m = self._mod - 1
            cnt2 = bsf(m)
            e = pow(self._root, m >> cnt2, self._mod)
            ie = pow(e, self._mod - 2, self._mod)
            for i in range(cnt2 - 1)[::-1]:
                es[i] = e
                ies[i] = ie
                e *= e
                e %= self._mod
                ie *= ie
                ie %= self._mod

            now = 1
            for i in range(cnt2 - 1):
                self._sum_e[i] = es[i] * now % self._mod
                now *= ies[i]
                now %= self._mod

        for ph in range(1, h + 1):
            w = 1 << (ph - 1)
            p = 1 << (h - ph)
            now = 1
            for s in range(w):
                offset = s << (h - ph + 1)
                for i in range(p):
                    left = a[i + offset]
                    right = a[i + offset + p] * now
                    a[i + offset] = (left + right) % self._mod
                    a[i + offset + p] = (left - right) % self._mod

                now *= self._sum_e[bsf(~s)]
                now %= self._mod

    def _butterfly_inv(self, a):
        n = len(a)
        h = ceil_pow2(n)
        if self._first2:
            self._first2 = False
            es = [0] * 30
            ies = [0] * 30
            m = self._mod - 1
            cnt2 = bsf(m)
            e = pow(self._root, m >> cnt2, self._mod)
            ie = pow(e, self._mod - 2, self._mod)
            for i in range(cnt2 - 1)[::-1]:
                es[i] = e
                ies[i] = ie
                e *= e
                e %= self._mod
                ie *= ie
                ie %= self._mod

            now = 1
            for i in range(cnt2 - 1):
                self._sum_ie[i] = ies[i] * now % self._mod
                now *= es[i]
                now %= self._mod

        for ph in range(1, h + 1)[::-1]:
            w = 1 << (ph - 1)
            p = 1 << (h - ph)
            inow = 1
            for s in range(w):
                offset = s << (h - ph + 1)
                for i in range(p):
                    left = a[i + offset]
                    right = a[i + offset + p]
                    a[i + offset] = (left + right) % self._mod
                    a[i + offset + p] = (
                        (self._mod + left - right) * inow % self._mod
                    )
                inow *= self._sum_ie[bsf(~s)]
                inow %= self._mod

    def convolution(self, a, b):
        n = len(a)
        m = len(b)
        if n*m == 0:
            return []

        if min(n, m) <= 60:
            if n < m:
                n, m = m, n
                a, b = b, a

            res = [0] * (n + m - 1)
            for i in range(n):
                for j in range(m):
                    res[i + j] += a[i] * b[j]
                    res[i + j] %= self._mod

            return res

        z = 1 << ceil_pow2(n + m - 1)
        a += [0] * (z - n)
        b += [0] * (z - m)
        self._butterfly(a)
        self._butterfly(b)
        for i in range(z):
            a[i] *= b[i]
            a[i] %= self._mod

        self._butterfly_inv(a)
        a = a[:n + m - 1]
        iz = pow(z, self._mod - 2, self._mod)
        for i in range(n + m - 1):
            a[i] *= iz
            a[i] %= self._mod

        return a

s = input()
t = input()
mod = 998244353

ls = len(s)
lt = len(t)
s0 = [0] * ls
s1 = [0] * ls
t0 = [0] * lt
t1 = [0] * lt

for i in range(ls):
    if s[i] == '0':
        s0[i] = 1
    else:
        s1[i] = 1
for i in range(lt):
    if t[i] == '0':
        t0[lt-i-1] = 1
    else:
        t1[lt-i-1] = 1

cv01 = Convolution(mod)
cnt01 = cv01.convolution(s0,t1)

cv10 = Convolution(mod)
cnt10 = cv10.convolution(s1,t0)

ans = lt
for i in range(lt-1, ls):
    tmp = cnt01[i] + cnt10[i]
    ans = min(ans,tmp)

print(ans)
# print(cnt01)
# print(cnt10)
# print(s0)
# print(s1)
# print(t0)
# print(t1)