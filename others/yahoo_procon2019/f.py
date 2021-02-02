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

s = input()
n = len(s)
mod = 998244353

rb_use = [[0]*(2*n+1)  for _ in range(2)]
r = 0
b = 0
for i in range(n):
    if(s[i]=='0'):
        r += 2
    elif(s[i]=='1'):
        r += 1
        b += 1
    else:
        b += 2
    rb_use[0][i+1] = rb_use[0][i]
    rb_use[1][i+1] = rb_use[1][i]
    if(r>0):
        rb_use[0][i+1] += 1
        r -= 1
    if(b>0):
        rb_use[1][i+1] += 1
        b -= 1

for i in range(n,2*n):
    rb_use[0][i+1] = rb_use[0][i]
    rb_use[1][i+1] = rb_use[1][i]
    if(r>0):
        rb_use[0][i+1] += 1
        r -= 1
    if(b>0):
        rb_use[1][i+1] += 1
        b -= 1

r_max = rb_use[0][-1]
b_max = rb_use[1][-1]

dp = [[0] * (b_max+1) for _ in range(r_max+1)]
dp[0][0] = 1

for i in range(r_max+1):
    for j in range(b_max+1):
        tot = i+j
        if(rb_use[0][tot] >= i)&(rb_use[1][tot] >= j):
            if(i==0)&(j==0):
                continue
            elif(i==0):
                dp[i][j] = dp[i][j-1]
            elif(j==0):
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = (dp[i][j-1] + dp[i-1][j])%mod

print(dp[-1][-1])


'''
02

rrbbの並び替えは4C2=6通り
そのうち作れないのは
bから始まるbbrr,brbr,brrb

1210
8c4 = 70

最初の二つが'12'なので
頭の2つにrrはできない
6c2＝15

引き算でどうにかしたい・・・

頭から、maxで使えるr,bの数をカウントしていく
あとはdpでうまく遷移していけるのでは

'''
