# a,b = map(int,input().split())
# a = list(map(int,input().split()))
# a = [list(map(int,input().split())) for _ in range(n)]

# import sys
# read = sys.stdin.buffer.read
# readline = sys.stdin.buffer.readline
# readlines = sys.stdin.buffer.readlines

# 検討?分　実装分 バグとり分

import sys
import os
f = open('../../input.txt', 'r')
sys.stdin = f

n,k = map(int,input().split())
a = list(map(int,input().split()))

a.sort(reverse=True)
dp = [False] * (k)
dp[0] = True
min_n = 10**10
for i in a:
    for j in range(k-1,-1,-1):
        if(dp[j]):
            if(j+i >= k):
                min_n = i
            else:
                dp[j+i] = True

ans = 0
for i in a:
    ans += (i < min_n)

print(ans)
