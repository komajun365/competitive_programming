# a,b = map(int,input().split())
# a = list(map(int,input().split()))
# a = [list(map(int,input().split())) for _ in range(n)]

import sys
import os
f = open('../../input.txt', 'r')
sys.stdin = f

n = int(input())
a = tuple(map(int, input().split()))

if(n <= 3):
    print(max(a))
    exit()

dp = [[0] * 2 for _ in range(n+1)]
dp[1][1] = a[0]
dp[2][1] = a[1]
dp[3][0] = a[2]
dp[3][1] = a[0] + a[2]

for i in range(4,n+1):
    if(i%2 == 0):
        dp[i][1] = a[i-1] + max(dp[i-2][1], dp[i-3][1])
    else:
        dp[i][0] = a[i-1] + max(dp[i-2][0], dp[i-3][1], dp[i-4][1])
        dp[i][1] = a[i-1] + dp[i-2][1]

if(n%2==0):
    ans = max(dp[-1][1], dp[-2][1])
else:
    ans = max(dp[-1][0], dp[-2][1], dp[-3][1])

print(ans)
