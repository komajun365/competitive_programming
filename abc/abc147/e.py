# a,b = map(int,input().split())
# a = list(map(int,input().split()))
# a = [list(map(int,input().split())) for _ in range(n)]

import sys
import os
f = open('../../input.txt', 'r')
sys.stdin = f

h,w = map(int,input().split())
a = [list(map(int,input().split())) for _ in range(h)]
b = [list(map(int,input().split())) for _ in range(h)]

for i in range(h):
    for j in range(w):
        a[i][j] = abs(a[i][j] - b[i][j])

dp = [[0] * 9600 for _ in range(w*h)]
for i in range(h):
    for j in range(w):
        min_ = max(0, 3200 - min(i+j, 160-i-j)*80)
        max_ = min(9599, 3200 + min(i+j, 160-i-j)*80)
        a_tmp = a[i][j]
        if(i==0)&(j==0):
            dp[i*w+j][3200+a_tmp] += 1
            dp[i*w+j][3200-a_tmp] += 1
        elif(i==0):
            for k in range(min_, max_+1):
                if(k+a_tmp < 9600):
                    dp[i*w+j][k+a_tmp] += dp[i*w+j-1][k]
                if(k-a_tmp >= 0):
                    dp[i*w+j][k-a_tmp] += dp[i*w+j-1][k]
        elif(j==0):
            for k in range(min_, max_+1):
                if(k+a_tmp < 9600):
                    dp[i*w+j][k+a_tmp] += dp[i*w+j-w][k]
                if(k+a_tmp >= 0):
                    dp[i*w+j][k-a_tmp] += dp[i*w+j-w][k]
        else:
            for k in range(min_, max_+1):
                if(k+a_tmp < 9600):
                    dp[i*w+j][k+a_tmp] += dp[i*w+j-1][k]
                    dp[i*w+j][k+a_tmp] += dp[i*w+j-w][k]
                if(k+a_tmp >= 0):
                    dp[i*w+j][k-a_tmp] += dp[i*w+j-1][k]
                    dp[i*w+j][k-a_tmp] += dp[i*w+j-w][k]

ans = 3200
for i in range(3100, 3300):
    if(dp[-1][i] > 0):
        ans = min(ans, abs(i-3200))

print(ans)
