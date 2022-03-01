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

n = int(input())
c = list(map(int,input().split()))
mod = 998244353

max_n = n + 100
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

# 二項係数の計算
def com(n,k):
    if(n < k):
        return 0
    if( (n<0) | (k < 0)):
        return 0
    return fac[n] * (finv[k] * finv[n-k] % mod) % mod

cnt = dict()
for ci in c:
    cnt[ci] = cnt.get(ci, 0) + 1

cnt2 = dict()
for x in cnt.values():
    cnt2[x] = cnt2.get(x,0) + 1

ans = [0] * (n+1)
for x,m in cnt2.items():
    for k in range(1,n+1):
        ans[k] += (com(n,k) - com(n-x,k)) * m % mod
        ans[k] %= mod

for k in range(1,n+1):
        ans[k] *= pow(com(n,k), mod-2, mod)
        ans[k] %= mod

print('\n'.join(map(str,ans[1:])))



