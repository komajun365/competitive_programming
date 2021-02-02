import sys
import os
f = open('../../input.txt', 'r')
sys.stdin = f

n,k = map(int, input().split())
a = list(map(int, input().split()))

dp = [0]*(k+1)

for i in range(a[0]):
    dp[i] = 2

for i in range(a[0],k+1):
    for j in a:
        if(j > i):
            dp[i] = 2
            break
        if(dp[(i-j)]==2):
            dp[i] = 1
            break
        dp[i] = 2

if(dp[k] == 1):
    print('First')
else:
    print('Second')
