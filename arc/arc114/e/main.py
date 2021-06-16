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

H,W = map(int,input().split())
h1,w1,h2,w2 = map(int,input().split())
mod = 998244353

n = (H-1) + (W-1)
a = min(h1,h2)-1
b = H - max(h1,h2)
c = min(w1,w2)-1
d = W - max(w1,w2)
e = n - a-b-c-d

max_n = H+W + 10
fac, finv, inv = [0]*max_n, [0]*max_n, [0]*max_n

def comInit(max_n):
    fac[0] = fac[1] = 1
    finv[0] = finv[1] = 1
    inv[1] = 1

    for i in range(2,max_n):
      fac[i] = fac[i-1]* i% mod
      inv[i] = mod - inv[mod%i] * (mod // i) % mod
      finv[i] = finv[i-1] * inv[i] % mod

comInit(max_n)


ans = 1
for x in [a,b,c,d]:
    for i in range(x):
        ans += fac[e+i] * finv[e+i+1]
        ans %= mod

print(ans)


# for k in range(1,a+b+c+d+2):
#     back = n-k
#     if back < e-1:
#         break

#     tmp = com(back, e-1)
#     tmp *= com(n-e,a)
#     tmp %= mod
#     tmp *= com(n-e-a,b)
#     tmp %= mod
#     tmp *= com(n-e-a-b,c)
#     tmp %= mod
#     ans += tmp * k
#     ans %= mod

# tot = com(n,a)
# tot *= com(n-a,b)
# tot %= mod
# tot *= com(n-a-b,c)
# tot %= mod
# tot *= com(n-a-b-c,d)
# tot %= mod
# ans *= pow(tot, mod-2,mod)
# ans %= mod

# print(ans)