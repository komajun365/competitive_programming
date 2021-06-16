# a,b = map(int,input().split())
# a = list(map(int,input().split()))
# a = [list(map(int,input().split())) for _ in range(n)]

import sys
import os
f = open('../../input.txt', 'r')
sys.stdin = f

n = int(input())
a = list(map(int,input().split()))
ai = [(val, ind) for ind,val in enumerate(a)]
ai.sort(reverse=True)

dp = [[0] * (n+1) for _  in  range(n+1)]
for i,tmp in enumerate(ai,1):
    val , val_i = tmp
    for right in range(i+1):
        left = i-right
        if(left==0):
            dp[left][right] = dp[left][right-1] + val * abs((n-right)  - val_i)
        elif(right==0):
            dp[left][right] = dp[left-1][right] + val * abs((val_i - (left-1)))
        else:
            dp[left][right] = max(dp[left][right-1] + val * abs((n-right)  - val_i),
                                    dp[left-1][right] + val * abs((val_i - (left-1))))


ans = 0
for i in range(n+1):
    ans = max(ans, dp[n-i][i])
print(ans)
