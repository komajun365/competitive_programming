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

import sys
read = sys.stdin.read

h,w,*s = read().split()
h = int(h)
w = int(w)

dp = [[-1] * (w+1) for _ in range(h+1)]
for i in range(h-1,-1,-1):
    for j in range(w-1,-1,-1):
        if(s[i][j] == '#'):
            continue

        tmp = 0
        for dx,dy in zip([0,1,1],[1,0,1]):
            dx += i
            dy += j
            if(dp[dx][dy] == 0):
                tmp = 1
        dp[i][j] = tmp

if(dp[0][0]==1):
    print('First')
else:
    print('Second')
