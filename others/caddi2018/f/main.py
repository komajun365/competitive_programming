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

n,m,*abc = map(int,read().split())
mod = 998244353

diag = dict()
outer = dict()
it = iter(abc)
for a,b,c in zip(it,it,it):
    a -= 1
    b -= 1
    if abs(a-b) <= 2:
        num = a*n + b
        diag[num] = c
    else:
        if a > b:
            a,b = b,a
        num = a*n + b
        if num in outer:
            if (outer[num] + c)%2 == 1:
                print(0)
                exit()
        else:
            outer[num] = c

dp = [[0] * 2 for _ in range(n)]
cnt = 0
tot = 0
for i in [0,1,n]:
    if i in diag:
        cnt += 1
        tot += diag[i]
if n+1 in diag:
    if cnt == 3:
        if (tot + diag[n+1]) % 2 == 0:
            dp[1][ diag[n+1] ] = 1
    else:
        dp[1][ diag[n+1] ] = 2 ** (2-cnt)
else:
    if cnt == 3:
        dp[1][tot % 2] = 1
    else:
        dp[1][0] = 2 ** (2-cnt)
        dp[1][1] = 2 ** (2-cnt)

for i in range(1,n-1):
    ur = n*(i-1) + i+1
    r = ur + n
    dr = r + n
    d = dr-1
    dl = d-1
    cnt = 0
    tot = 0
    for k in [r,d]:
        if k in diag:
            cnt += 1
            tot += diag[k]
    for j in range(2):
        mul = 1
        if ur in diag and dl in diag:
            if (j + diag[ur] + diag[dl]) % 2 == 1:
                continue
        elif not (ur in diag or dl in diag):
            mul = 2
        
        if dr in diag:
            if cnt == 2:
                if (tot + j + diag[dr]) % 2 == 0:
                    dp[i+1][diag[dr]] += dp[i][j] * mul
            else:
                dp[i+1][diag[dr]] += dp[i][j] * mul * 2 ** (1-cnt)
        else:
            if cnt == 2:
                dp[i+1][ (j + tot) % 2 ] += dp[i][j] * mul
            else:
                dp[i+1][0] += dp[i][j] * mul * 2 ** (1-cnt)
                dp[i+1][1] += dp[i][j] * mul * 2 ** (1-cnt)
    dp[i+1][0] %= mod
    dp[i+1][1] %= mod

ans = sum(dp[-1]) % mod

if n > 3:
    free = (n**2 - 9 - 5*(n-3))//2
    free -= len(outer)
    ans *= pow(2,free,mod)
    ans %= mod

print(ans)
        
