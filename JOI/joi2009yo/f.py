# a,b = map(int,input().split())
# a = list(map(int,input().split()))
# a = [list(map(int,input().split())) for _ in range(n)]

# 検討35分　実装10分 バグとり10分

import sys
import os
f = open('../../input.txt', 'r')
sys.stdin = f

import gc

n,m,s = map(int,input().split())
n = n**2
mod = 10**5

dp = [0] * (m+1)
for j in range(m+1):
    dp[j] = [0]*(s+1)

def update(dp):
    res = [0] * (m+1)
    for j in range(m+1):
        res[j] = [0]*(s+1)

    for j in range(1,m+1):
        for k in range(1,s+1):
            if(k-j>=0):
                res[j][k] = (res[j-1][k-1] + dp[j-1][k-j])%mod
    return res

dp[0][0] = 1
for i in range(1,n+1):
    dp = update(dp)
    gc.collect()

ans = 0
for j in range(1,m+1):
    ans += dp[j][-1]

ans %= mod
print(ans)

# 下記はMLE
# n,m,s = map(int,input().split())
# n = n**2
# mod = 10**5
#
# dp = [0] * (n+1)
# for i in range(n+1):
#     dp[i] = [0]*(m+1)
#     for j in range(m+1):
#         dp[i][j] = [0]*(s+1)
#
# dp[0][0][0] = 1
# for i in range(1,n+1):
#     for j in range(1,m+1):
#         for k in range(1,s+1):
#             if(k-j>=0):
#                 dp[i][j][k] = (dp[i][j-1][k-1] + dp[i-1][j-1][k-j])%mod
#
# ans = 0
# for j in range(1,m+1):
#     ans += dp[-1][j][-1]
#
# ans %= mod
# print(ans)

'''
1~Mの整数N**2個の合計がSである。
整数の選び方組み合わせを答えよ。
典型っぽいが。。。

N**2～1までの数字を並べた数列aを考える
また、広義単調減少で、0以上の数列b（長さN**2）を考える。
c(i)=a(i)+b(i)とすれば、
c(i)は重複のない協議単調減少数列になる。
→数列bの作り方組み合わせ数の問題に落ちる。

時間長いし愚直にdpで良いか？
数字i個を使って、
最大値jを加えたとき
合計がkとなる組み合わせの数

dp[i][j][k] = Σ　dp[i-1][J'][k-j] ※j'はj未満のものすべて
dp[i][j-1][k-1] = Σ　dp[i-1][J'][k-j]
dp[i][j][k] = dp[i][j-1][k-1] + dp[i-1][j-1][k-j]

dp[1][1][1] = dp[1][0][0] + dp[0][0][0]
dp[1][2][2] = dp[1][1][1] + dp[0][1][0]
dp[1][3][3] = dp[1][2][2] + dp[0][2][0]

'''
