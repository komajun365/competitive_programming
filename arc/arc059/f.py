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
s = input()
mod = 10**9+7

dp = [[0] * (n+1) for _ in range(n+1)]
dp[0][0] = 1

for i in range(n):
    for j in range(n):
        if(j==0):
            dp[i+1][0] += dp[i][0]
            dp[i+1][0] %= mod
            dp[i+1][1] += dp[i][0]*2
            dp[i+1][1] %= mod
        else:
            dp[i+1][j-1] += dp[i][j]
            dp[i+1][j-1] %= mod
            dp[i+1][j+1] += dp[i][j]*2
            dp[i+1][j+1] %= mod

ans = dp[-1][len(s)] * pow(pow(2,mod-2,mod),len(s),mod)
ans %= mod
print(ans)

for i in dp:
    print(i)

'''
dp[i][j] := 今i文字入力されていて、j文字目まで正しい

sn := len(s)
k := n-sn

k回分の遊び、がある。
・遊び
A.コスト1：先頭でバックスペースを押す
B.コスト2：1文字入力してすぐ消す
C.コスト4：

dp[i][j]:= i文字入力済で、j回キーを押した（不可逆）

cost[i][j] :=



'''
