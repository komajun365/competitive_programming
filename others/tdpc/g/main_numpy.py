# oj t -c "python main.py" -d "./tests/" 

# a,b = map(int,input().split())
# a = list(map(int,input().split()))
# a = [list(map(int,input().split())) for _ in range(n)]

# import sys
# read = sys.stdin.buffer.read
# readline = sys.stdin.buffer.readline
# readlines = sys.stdin.buffer.readlines

# 検討?分　実装分 バグとり分

# import sys
# import os
# f = open('../../../input.txt', 'r')
# sys.stdin = f

import numpy as np
from numba import njit

s = input()
k = int(input())
n = len(s)

s2 = []
for si in s:
    s2.append(ord(si)-ord('a'))
s,s2 = s2,s

@njit
def make_next_ch():
    next_ch = np.full((26,n+1),-1)
    print(next_ch)
    for i,si in enumerate(s):
        next_ch[si,i-1] = i
    for i in range(26):
        for j in range(n-3,-2,-1):
            if next_ch[i,j] == -1:
                next_ch[i,j] = next_ch[i,j+1]
    return next_ch

next_ch = make_next_ch()

@njit
def calc_dp():
    inf = 10**18 + 5
    dp = np.ones(n+1, dtype='int64')
    for i in range(n-1,-2,-1):
        for j in range(26):
            if next_ch[j][i] == -1:
                continue
            dp[i] += dp[next_ch[j][i]]
            if dp[i] >= inf:
                dp[i] = inf
                break
    return dp

dp = calc_dp()

if dp[-1]-1 < k:
    print('Eel')
    exit()

x = k
ans = ''
idx = -1
while x > 0:
    for i in range(26):
        idx2 = next_ch[i][idx]
        if idx2 == -1:
            continue
        if dp[idx2] >= x:
            ans += chr(ord('a') + i)
            idx = idx2
            x -= 1
            break
        x -= dp[idx2]

print(ans)