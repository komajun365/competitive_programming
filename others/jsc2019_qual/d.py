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

n = int(input())

def calc(i,j):
    x = i^j
    for k in range(20):
        if((x>>k)&1):
            return k+1

ans = [[0]*n for _ in range(n)]
for i in range(n-1):
    for j in range(i+1,n):
        ans[i][j] = calc(i,j)

for i in range(n-1):
    print(' '.join(map(str,ans[i][i+1:])))
