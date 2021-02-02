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
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

l = int(readline())
a = list(map(int,read().split()))

dp = [[0] * (l+1) for _ in range(5)]

for i in range(l):
    dp[0][i+1] = dp[0][i] + a[i]

for i in range(l):
    dp[1][i+1] = min(dp[0][i+1],
                    min(dp[0][i], dp[1][i]) + (a[i]%2 if a[i]!=0 else 2))

for i in range(l):
    dp[2][i+1] = min(dp[1][i+1],
                    min(dp[0][i], dp[1][i], dp[2][i]) + (a[i]-1)%2)

for i in range(l):
    dp[3][i+1] = min(dp[2][i+1],
                    min(dp[0][i], dp[1][i], dp[2][i], dp[3][i]) + (a[i]%2 if a[i]!=0 else 2))

for i in range(l):
    dp[4][i+1] = min(dp[3][i+1],
                    min(dp[0][i], dp[1][i], dp[2][i], dp[3][i], dp[4][i]) + a[i])

print(dp[-1][-1])

# for i in dp:
#     print(i)

'''
噂の耳DPか？

りんごさんの旅が
iから初めてjで終わるとする
i <= jとしておく。
・iより左
偶数回処理できる。
・i
奇数回処理できる
・i < x < j
奇数回
・j
偶数回
・jより右
偶数回

?=0含む、#=0含まない　とする。
0*? + even*? + odd*? + even*? + 0*?
が作れる形？

dp[i][j] := jまで決めうちで処理したときのりんごさん対応回数とする。


'''
