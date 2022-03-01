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



n,x,y,z = map(int,input().split())
mod = 998244353

if (n-x-y-z) % 2 == 1:
    print(0)
    exit()

## nCkのmodを求める関数
# テーブルを作る(前処理)
max_n = n+10
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

x = abs(x)
y = abs(y)
z = abs(z)

ans = 0
for xp in range(x,n+1):
    xm = xp-x
    n2 = n-xp-xm
    rem = n2-y-z
    if rem < 0:
        break
    plus = y + z + rem//2
    ans += ((com(n,xp) * com(n-xp,xm)) % mod)  * (com(n2, y + rem//2) * com(n2,rem//2) % mod)
    ans %= mod
print(ans)

