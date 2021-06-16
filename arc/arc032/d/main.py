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

n,k,*m = map(int,read().split())
mod = 1000000007
size = 3001
# size = 5

max_n = n + 10
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

cs = [[0] * (size+1) for _ in range(size+1)]

it = iter(m)
for ma,md in zip(it,it):
    cs[ma][md] += 1

for i in range(size):
    for j in range(1,size):
        cs[i][j] += cs[i][j-1]

for i in range(1,size):
    for j in range(size):
        cs[i][j] += cs[i-1][j]

def get_cnt(i,j,x):
    res = cs[i+x][j+x] - cs[i-1][j+x] - cs[i+x][j-1] + cs[i-1][j-1]
    return res

def check(x):
    for i in range(size-x):
        for j in range(size-x):
            if cs[i+x][j+x] - cs[i-1][j+x] - cs[i+x][j-1] + cs[i-1][j-1] >= k:
                return True
    return False

ok = 3000
ng = -1
while ok-ng > 1:
    mid = (ok+ng)//2
    if check(mid):
        ok = mid
    else:
        ng = mid

ans = 0
for i in range(size):
    for j in range(size):
        i2 = min(size-1, i+ok)
        j2 = min(size-1, j+ok)
        cnt1 = cs[i2][j2] - cs[i-1][j2] - cs[i2][j-1] + cs[i-1][j-1]
        cnt2 = cs[i2][j2] - cs[i-1][j2] - cs[i2][j] + cs[i-1][j]
        cnt3 = cs[i2][j2] - cs[i][j2] - cs[i2][j-1] + cs[i][j-1]
        ans += com(cnt1,k) - com(cnt2,k) - com(cnt3,k)
        ans %= mod
        # print(i,j,cnt1,cnt2)

print(ok)
print(ans)

