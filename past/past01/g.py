# a,b = map(int,input().split())
# a = list(map(int,input().split()))
# a = [list(map(int,input().split())) for _ in range(n)]

# 検討?分　実装分 バグとり分

import sys
import os
f = open('../../input.txt', 'r')
sys.stdin = f

import itertools

n=int(input())
a = [list(map(int,input().split())) for _ in range(n-1)]

ans = -1 * (10**10)
it = itertools.product([0,1,2], repeat=n)
for pattern in it:
    calc = 0
    for i in range(n-1):
        for j in range(i+1,n):
            if(pattern[i]==pattern[j]):
                calc += a[i][j-i-1]
    ans = max(ans,calc)

print(ans)
