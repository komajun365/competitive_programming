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

flag = 0
start = 0
for i in range(k-1):
    if(a[i+1] - a[i] in [1,3,5]):
        flag=1
        start = a[i+1]

if(flag==0):
    print('Yes')
    exit()

if(start > 20):
    print('No')
    exit()

dp = [0] * (min(n,start)+1)
for ai in a:
    if(ai > start):
        break
    dp[ai] = 1

for i in range(len(dp)-1,0,-1):
    if(dp[i]==0):
        continue
    for j,b in zip([i-1,i-3,i-5],[i-4,i-5,i-6]):
        if(j>0)&(b>0):
            if(dp[j]==1):
                dp[b] = 1

if(dp[1]==1):
    print('No')
else:
    print('Yes')

print(dp)
