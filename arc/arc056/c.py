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

n,K = map(int,input().split())
w = [list(map(int,input().split())) for _ in range(n)]

sum_w = [0] * (2**n)
for i in range(n):
    for j in range(2**i):
        sum_w[j+2**i] = sum_w[j]
        for k in range(i):
            if(j>>k)&1:
                sum_w[j+2**i] += w[i][k]


inf = -1 * 10**10
dp = [inf] * (2**n)
dp[-1] = 0
for i in range(2**n-1,0,-1):
    x = i
    while(x>0):
        x = (x-1)&i
        dp[x] = max(dp[x], dp[i] + K + sum_w[x] + sum_w[i^x] - sum_w[i])

print(max(dp))





'''
dp[i][j] := iチーム作って、残りのメンバがjの時の最高スコア　（jは暫定的に一つのチームとする）

dp[i][j] -> dp[i+1][k]
チームが増えたので＋K
jが解散してので、信頼度の和をマイナス
j^k とkができたので、信頼度の和をプラス

遷移が多い。
(jの1の数)**2 - 1通りの遷移がある。

Σ nCk * (2**k) = (1+2)**n
3**17　≒　1.2*10**8

ちょっと無理がある。

dp[i+1][k]がどこから遷移してくるべきなのかがO(1)でわかればいい
jとj^kで決まるはず


dpの1次元目は不要っぽい。
3秒だし、1.2*10**8だけでいけるか？



'''
