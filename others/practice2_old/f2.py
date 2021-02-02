# a,b = map(int,input().split())
# a = list(map(int,input().split()))
# a = [list(map(int,input().split())) for _ in range(n)]

# import sys
# read = sys.stdin.buffer.read
# readline = sys.stdin.buffer.readline
# readlines = sys.stdin.buffer.readlines

# 検討?分　実装分 バグとり分

import sys
import os
f = open('../../input.txt', 'r')
sys.stdin = f


class Convolution():
    def __init__(self, mod: int):
        self.__mod = mod
        self.__g = self.primitive_root(mod)
        self.__first_butterfly = True
        self.__first_butterfly_inv = True
        self.__sum_e = [0] * 30
        self.__sum_ie = [0] * 30

    # @param n `0 <= n`
    # @return minimum non-negative `x` s.t. `n <= 2**x`
    def ceil_pow2(self, n: int):
        x = 0
        while((1 << x) < n):
            x += 1
        return x

    # @param n `1 <= n`
    # @return minimum non-negative `x` s.t. `(n & (1 << x)) != 0`
    def bsf(self, n: int):
        assert 1 <= n
        x = 0
        while((1 << x) & n) == 0:
            x += 1
        return x

    # @param n `0 <= n`
    # @return minimum non-negative `x` s.t. `(n & (1 << x)) == 0`
    def bsf_0(self, n: int):
        assert 0 <= n
        x = 0
        while((n >> x) & 1):
            x += 1
        return x

    # 原始根の取得
    def primitive_root(self, m):
        if (m == 2):
            return 1
        if (m == 167772161):
            return 3
        if (m == 469762049):
            return 3
        if (m == 754974721):
            return 11
        if (m == 998244353):
            return 3
        divs = [0] * 20
        divs[0] = 2
        cnt = 1
        x = (m-1)//2
        while(x % 2 == 0):
            x //= 2
        for i in range(3, x+1, 2):
            if(i**2 > x):
                break
            if(x % i == 0):
                divs[cnt] = i
                cnt += 1
                while(x % i == 0):
                    x //= i
        if(x > 1):
            divs[cnt] = x
            cnt += 1
        g = 2
        while(True):
            ok = True
            for i in range(cnt):
                if(pow(g, (m-1)//divs[i], m) == 1):
                    ok = False
                    break
            if(ok):
                return g
            g += 1

    def butterfly(self, a: list):
        mod = self.__mod
        n = len(a)
        h = (n-1).bit_length()
        if(self.__first_butterfly):
            self.__first_butterfly = False
            es = [0] * 30
            ies = [0] * 30
            cnt2 = self.bsf(mod - 1)
            e = pow(self.__g, (mod-1) >> cnt2, mod)
            ie = pow(e, mod-2, mod)
            for i in range(cnt2, 1, -1):
                es[i-2] = e
                ies[i-2] = ie
                e *= e
                e %= mod
                ie *= ie
                ie %= mod
            now = 1
            for i in range(cnt2-1):
                self.__sum_e[i] = (es[i] * now) % mod
                now *= ies[i]
                now %= mod
        for ph in range(1, h+1):
            w = 1 << (ph-1)
            p = 1 << (h-ph)
            now = 1
            for s in range(w):
                offset = s << (h-ph+1)
                for i in range(p):
                    l = a[i + offset]
                    r = (a[i + offset + p] * now) % mod
                    a[i + offset] = (l+r) % mod
                    a[i + offset + p] = (l-r) % mod
                now *= self.__sum_e[self.bsf_0(s)]
                now %= mod

    def butterfly_inv(self, a: list):
        mod = self.__mod
        n = len(a)
        h = (n-1).bit_length()
        if(self.__first_butterfly_inv):
            self.__first_butterfly_inv = False
            es = [0] * 30
            ies = [0] * 30
            cnt2 = self.bsf(mod - 1)
            e = pow(self.__g, (mod-1) >> cnt2, mod)
            ie = pow(e, mod-2, mod)
            for i in range(cnt2, 1, -1):
                es[i-2] = e
                ies[i-2] = ie
                e *= e
                e %= mod
                ie *= ie
                ie %= mod
            now = 1
            for i in range(cnt2-1):
                self.__sum_ie[i] = (ies[i] * now) % mod
                now *= es[i]
                now %= mod
        for ph in range(h, 0, -1):
            w = 1 << (ph-1)
            p = 1 << (h-ph)
            inow = 1
            for s in range(w):
                offset = s << (h-ph+1)
                for i in range(p):
                    l = a[i + offset]
                    r = a[i + offset + p]
                    a[i + offset] = (l+r) % mod
                    a[i + offset + p] = ((mod + l - r) * inow) % mod
                inow *= self.__sum_ie[self.bsf_0(s)]
                inow %= mod

    def convolution(self, a: list, b: list):
        mod = self.__mod
        n = len(a)
        m = len(b)
        if(n == 0) | (m == 0):
            return []
        if(min(n, m) <= 60):
            if(n < m):
                a, b = b, a
                n, m = m, n
            ans = [0] * (n+m-1)
            for i in range(n):
                for j in range(m):
                    ans[i+j] += a[i] * b[j]
                    ans[i+j] %= mod
            return ans

        z = (1 << (n+m-2).bit_length())
        a += [0] * (z-n)
        self.butterfly(a)
        b += [0] * (z-m)
        self.butterfly(b)
        for i in range(z):
            a[i] *= b[i]
            a[i] %= mod
        self.butterfly_inv(a)
        a = a[:(n+m-1)]
        iz = pow(z, mod-2, mod)
        for i in range(n+m-1):
            a[i] *= iz
            a[i] %= mod
        return a

n,m = map(int,input().split())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
mod = 998244353

cv = Convolution(mod)
c = cv.convolution(a,b)
print(*c)
