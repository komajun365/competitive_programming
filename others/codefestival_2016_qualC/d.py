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

h,w = map(int,input().split())
c = [input() for _ in range(h)]

ans = 0
for i in range(w-1):
    cost = [[0] * (h+1) for _ in range(h+1)]
    for ci in range(1,h+1):
        for cj in range(ci,h+1):
            cost[ci][cj] = cost[ci-1][cj-1] + (c[ci-1][i] == c[cj-1][i+1])

    for cj in range(1,h+1):
        for ci in range(cj+1,h+1):
            cost[ci][cj] = cost[ci-1][cj-1] + (c[ci-1][i] == c[cj-1][i+1])

    dp = [[0] * (h+1) for _ in range(h+1)]
    for ci in range(1,h+1):
        for cj in range(1,h+1):
            dp[ci][cj] = min(dp[ci-1][cj], dp[ci][cj-1]) + cost[ci][cj]

    ans += dp[-1][-1]

print(ans)






'''
abc
bca

え、むずい

2列だけだったら？
→　N**2で計算できる。
→　くわしく！
　　calc(0,0) = 0
    calc(i,j) = min( calc(i-1,j) + ??? , calc(i,j-1) + ???)
    ???は一緒。
    i>jとして、
    1列目の[(i-j)-(i-1)]と2列目の[0-(j-1)]を比較したときの値があればよい。
    cost[i][j]で前計算しておけばいい。

3列を2*N**2でできるか？

[1,2,2,2,1,1]
[3,3,2,3,2,2]
-> 1,3,3,2,3,2,2,1,1,

(n-1)個の部分列を仕込めますか？という問題。
そりゃできる！


'''
