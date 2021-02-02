import sys
import os
f = open('../../input.txt', 'r')
sys.stdin = f

import bisect

n = int(input())
h = list(map(int, input().split()))
a = list(map(int, input().split()))

bis = [0]
dp = [0]*(n+1)

for i in range(n):
    max_point = bisect.bisect_left(bis, h[i]) -1
    dp[h[i]] = dp[ bis[max_point] ] + a[i]
    bisect.insort_left(bis, h[i])

print(max(dp))
