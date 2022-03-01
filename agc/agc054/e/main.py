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

import sys
read = sys.stdin.buffer.read

t,*na = map(int,read().split())
mod = 998244353

max_n = 10**6
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

def solve(n,a):
    if n == 3:
        tmp = [1,2,1]
        return tmp[a-1]
    if a > 2 and a < n-1:
        res = fac[n-1] - fac[n-2] * 2
        res %= mod

        res += fac[n-3] * (n-1) 
        res %= mod
        return res
    
    
    if a == 1 or a == n:
        a = 1
        res = fac[n-1] - fac[n-2]*2
        res %= mod
        res += fac[n-3]
        res %= mod
    else:
        a = 2
        res = fac[n-1] - fac[n-2] * 2
        res %= mod

        res += fac[n-3]
        res %= mod
        
        res += fac[n-4]
        res %= mod

        res += fac[n-3] *2 - fac[n-4]
        res %= mod
    return res

ans = []
it = iter(na)
for n,a in zip(it,it):
    ans.append(solve(n,a))
print('\n'.join(map(str,ans)))


