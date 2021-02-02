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

dp = [0] * (n+1)
dp[0] = 1

for i in range(n):
    next = [0] * (n+1)
    for j in range(n):
        if(j==0):
            next[0] += dp[0]
            next[0] %= mod
            next[1] += dp[0]*2
            next[1] %= mod
        else:
            next[j-1] += dp[j]
            next[j-1] %= mod
            next[j+1] += dp[j]*2
            next[j+1] %= mod
    dp = next[::]

ans = dp[len(s)] * pow(pow(2,mod-2,mod),len(s),mod)
ans %= mod
print(ans)


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
