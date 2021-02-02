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

n = int(input())
a = list(map(int, input().split()))
p = 200003
root = 2

encode = [0] * p # x -> root**y
decode = [0] * (p-1)

x = 1
for i in range(p-1):
    encode[x] = i
    decode[i] = x
    x = x*root % p

cnt = [0] * (p-1)
for ai in a:
    if(ai==0):
        continue
    cnt[ encode[ai] ] += 1


cnt_l = [i % 1000  for i in cnt]
cnt_r = [i // 1000  for i in cnt]

prod = [0] * (p-1)
for A,B,mul in zip([cnt_l,cnt_l,cnt_r,cnt_r],[cnt_l,cnt_r,cnt_l,cnt_r],[1,1000,1000,1000000]):
    a = A[::]
    b = B[::]
    cv = Convolution()
    res = cv.convolution(a,b)
    for i,ri in enumerate(res):
        prod[i%(p-1)] += ri*mul

for i,ci in enumerate(cnt):
    prod[i*2%(p-1)] -= ci

ans = 0
for i,pi in enumerate(prod):
    ans += pi//2 * decode[i]

print(ans)
