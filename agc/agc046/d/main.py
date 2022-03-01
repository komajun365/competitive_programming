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

s = input()
n = len(s)
mod = 998244353

max_n = 1000
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

dp = []
inf = 1000
for i in range(n):
    dp.append( [[inf,-1*inf] for _ in range(n+1)] )
dp[0][0] = [0,0]

ans = n
for i in range(1,n):
    for j in range(i+1,n+1):
        dp[i][j] = dp[i-1][j-1][:]
        if s[j-1] == '0':
            dp[i][j][1] = max(dp[i][j][1], min(dp[i-1][j-1][1] + 1, j-i))
        if s[j-1] == '1':
            dp[i][j][0] = min(dp[i][j][0], max(dp[i-1][j-1][0] - 1, 0))
        if s[j-2:j] == '00':
            dp[i][j][0] = min(dp[i][j][0], dp[i-1][j-2][0] + 1)
            dp[i][j][1] = max(dp[i][j][1], dp[i-1][j-2][1] + 1)
        elif s[j-2:j] == '11':
            dp[i][j][0] = min(dp[i][j][0], dp[i-1][j-2][0])
            dp[i][j][1] = max(dp[i][j][1], dp[i-1][j-2][1])
        else:
            dp[i][j][0] = min(dp[i][j][0], dp[i-1][j-2][0])
            dp[i][j][1] = max(dp[i][j][1], dp[i-1][j-2][1] + 1)
        
        if s[j-1] == '0':
            for k in range(dp[i][j][0], dp[i][j][1]+1):
                ans += com(j-i-1,k)
                ans %= mod
        else:
            for k in range(dp[i][j][0]-1, dp[i][j][1]):
                ans += com(j-i-1,k)
                ans %= mod
        # print(i,j,ans)
print(ans)





            