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

MOD = 998244353
class Convolution:
    def __init__(self):
        # self.mod = mod
        self.g = self.primitive_root(MOD)
        self.first_butterfly = True
        self.first_butterfly_inv = True
        self.sum_e = [0] * 30
        self.sum_ie = [0] * 30

    # 原始根の取得
    def primitive_root(self, m: int):
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

        print('error')
        return 0

    def butterfly(self, a: list):
        # MOD = self.mod
        n = len(a)
        h = (n-1).bit_length()
        if(self.first_butterfly):
            self.first_butterfly = False
            es = [0] * 30
            ies = [0] * 30
            mod_m = MOD-1
            cnt2 = (mod_m & -mod_m).bit_length() - 1
            e = pow(self.g, mod_m >> cnt2, MOD)
            ie = pow(e, MOD-2, MOD)
            for i in range(cnt2-2, -1, -1):
                es[i] = e
                ies[i] = ie
                e *= e
                e %= MOD
                ie *= ie
                ie %= MOD
            now = 1
            for i in range(cnt2-1):
                self.sum_e[i] = (es[i] * now) % MOD
                now *= ies[i]
                now %= MOD
        for ph in range(1, h+1):
            w = 1 << (ph-1)
            p = 1 << (h-ph)
            now = 1
            for s in range(w):
                offset = s << (h-ph+1)
                for i in range(p):
                    l = a[i + offset]
                    r = a[i + offset + p] * now
                    a[i + offset] = (l+r) % MOD
                    a[i + offset + p] = (l-r) % MOD
                now *= self.sum_e[(~s & -~s).bit_length() - 1]
                now %= MOD

    def butterfly_inv(self, a: list):
        # MOD = self.mod
        n = len(a)
        h = (n-1).bit_length()
        if(self.first_butterfly_inv):
            self.first_butterfly_inv = False
            es = [0] * 30
            ies = [0] * 30
            mod_m = MOD-1
            cnt2 = (mod_m & -mod_m).bit_length() - 1
            e = pow(self.g, mod_m >> cnt2, MOD)
            ie = pow(e, MOD-2, MOD)
            for i in range(cnt2-2, -1, -1):
                es[i] = e
                ies[i] = ie
                e *= e
                e %= MOD
                ie *= ie
                ie %= MOD
            now = 1
            for i in range(cnt2-1):
                self.sum_ie[i] = (ies[i] * now) % MOD
                now *= es[i]
                now %= MOD
        for ph in range(h, 0, -1):
            w = 1 << (ph-1)
            p = 1 << (h-ph)
            inow = 1
            for s in range(w):
                offset = s << (h-ph+1)
                for i in range(p):
                    l = a[i + offset]
                    r = a[i + offset + p]
                    a[i + offset] = (l+r) % MOD
                    a[i + offset + p] = ((l - r) * inow) % MOD
                inow *= self.sum_ie[(~s & -~s).bit_length() - 1]
                inow %= MOD

    def convolution(self, a: list, b: list):
        # MOD = self.mod
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
                    ans[i+j] %= MOD
            return ans

        z = 1 << (n+m-2).bit_length()
        a += [0] * (z-n)
        b += [0] * (z-m)
        self.butterfly(a)
        self.butterfly(b)
        for i in range(z):
            a[i] *= b[i]
            a[i] %= MOD
        self.butterfly_inv(a)
        a = a[:(n+m-1)]
        iz = pow(z, MOD-2, MOD)
        for i in range(n+m-1):
            a[i] *= iz
            a[i] %= MOD
        return a

    def convolution_ll(self, a: list, b: list):
        from math import gcd
        global MOD
        n = len(a)
        m = len(b)
        if(n == 0) | (m == 0):
            return []

        MOD1 = 754974721  # 2^24
        MOD2 = 167772161  # 2^25
        MOD3 = 469762049  # 2^26
        M2M3 = MOD2 * MOD3
        M1M3 = MOD1 * MOD3
        M1M2 = MOD1 * MOD2
        M1M2M3 = MOD1 * MOD2 * MOD3

        i1 = gcd(M2M3, MOD1) * pow(M2M3 % MOD1, MOD1-2, MOD1) % MOD1
        i2 = gcd(M1M3, MOD2) * pow(M1M3 % MOD2, MOD2-2, MOD2) % MOD2
        i3 = gcd(M1M2, MOD3) * pow(M1M2 % MOD3, MOD3-2, MOD3) % MOD3

        MOD = MOD1
        A = a[::]
        B = b[::]
        self.__init__()
        c1 = self.convolution(A, B)
        MOD = MOD2
        # A = a[::]
        # B = b[::]
        self.__init__()
        c2 = self.convolution(A, B)
        MOD = MOD3
        # A = a[::]
        # B = b[::]
        self.__init__()
        c3 = self.convolution(A, B)

        c = [0] * (n+m-1)
        for i in range(n+m-1):
            x = 0
            x += (c1[i] * i1) % MOD1 * M2M3
            x += (c2[i] * i2) % MOD2 * M1M3
            x += (c3[i] * i3) % MOD3 * M1M2
            c[i] = x % M1M2M3

        return c

import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

n,*data = map(int,read().split())
a = [0] + data[::2]
b = [0] + data[1::2]

cv = Convolution()
ans = cv.convolution(a,b)
print('\n'.join(map(str,ans[1:])))

# print(ans)
