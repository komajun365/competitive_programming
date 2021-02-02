import sys
import os
f = open('../../input.txt', 'r')
sys.stdin = f

h,w = map(int,input().split())
s = [input() for _ in range(h)]

dp = [[0] * w for _ in range(h)]
if(s[0][0] == '#'):
    dp[0][0] = 1

for i in range(h):
    for j in range(w):
        if(i == 0)&(j != 0):
            dp[i][j] = dp[i][j-1] + (s[i][j-1] != s[i][j])*1
        elif(i != 0)&(j == 0):
            dp[i][j] = dp[i-1][j] + (s[i-1][j] != s[i][j])*1
        elif(i != 0)&(j != 0):
            dp[i][j] =min(dp[i][j-1] + (s[i][j-1] != s[i][j])*1,
                            dp[i-1][j] + (s[i-1][j] != s[i][j])*1)

ans = (dp[-1][-1] + 1)//2
print(ans)
