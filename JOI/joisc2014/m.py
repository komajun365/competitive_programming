# a,b = map(int,input().split())
# a = list(map(int,input().split()))
# a = [list(map(int,input().split())) for _ in range(n)]

# 検討22分　実装8分 バグとり3分

import sys
import os
f = open('../../input.txt', 'r')
sys.stdin = f

import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

n = int(readline())
it = iter(map(int,read().split()))
ab = [(a,b)  for a,b in zip(it,it)]
ab.sort(reverse=True)

inf = -1 * 10**12
dp = [[inf] * (n+1) for _ in range(n+1)]
dp[0][1] = 0

for i in range(n):
    ai,bi = ab[i]
    for j in range(n+1):
        dp[i+1][j] = max(dp[i+1][j], dp[i][j])
        k = min(n, j-1+ai)
        if( k >= 0 ):
            dp[i+1][k] = max(dp[i+1][k], dp[i][j] + bi)

print(max(dp[-1]))

'''
方針
dp[i][j] : i番目までのストラップまで確認し、残りj個のストラップ穴があるとき、嬉しさの最大値
（ただし、ストラップは穴の数が多いものから処理する。）

i番目のストラップ（Ai,Bi）を処理するとき
dp[i+1][j] = max(dp[i+1][j], dp[i][j])と
dp[i+1][j-1+Ai] = max(dp[i+1][j-1+Ai], dp[i][j] + Bi)で更新できる。

ただし、使えるストラップ穴の数がn個を超えると全てのストラップを付けることができるようになることに気を付けると、
j-1+Ai　>= n のときはnに置き換えるといい。

max(dp[-1])が答え。
dpのサイズは(n+1)*(n+1)で、計算量はO(N**2)

'''
