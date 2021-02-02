import sys
import os
f = open('../../input.txt', 'r')
sys.stdin = f

n,k = map(int, input().split())
h = list(map(int, input().split()))

dp = [0]*n

for i in range(1,n):
    temp = 10**10
    for j in range(1, min(k+1, i+1) ):
        temp = min(temp, abs(h[i] - h[i-j]) + dp[i-j])
    dp[i] = temp

print(dp[n-1])
