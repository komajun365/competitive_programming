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

import random

import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

n = int(readline())
a = list(map(int,read().split()))
mod = 998244353

sum_a = sum(a)
dp = [ [0] * (sum_a+1) for _ in range(n+1)]
dp_rg = [ [0] * (sum_a+1) for _ in range(n+1)]
dp_rb = [ [0] * (sum_a+1) for _ in range(n+1)]
dp_r = [ [0] * (sum_a+1) for _ in range(n+1)]
dp_r[0][0] = 1
tot = 0

for i in range(1,n+1):
    ai = a[i-1]
    tot += ai
    for j in range(tot+1):
        dp_rg[i][j] += dp_rg[i-1][j] + dp_r[i-1][j]
        dp_rb[i][j] += dp_rb[i-1][j] + dp_r[i-1][j]
        dp[i][j] += dp[i-1][j] * 2 + dp_rb[i-1][j] + dp_rg[i-1][j]

        if(j >= ai):
            dp_r[i][j] += dp_r[i-1][j-ai]
            dp_rg[i][j] += dp_rg[i-1][j-ai]
            dp_rb[i][j] += dp_rb[i-1][j-ai]
            dp[i][j] += dp[i-1][j-ai]
        dp_rg[i][j] %= mod
        dp_rb[i][j] %= mod
        dp[i][j] %= mod

r_over = sum(dp[-1][(1+sum_a)//2:]) % mod
ans = (pow(3,n,mod) - 3*pow(2,n,mod) + 3 - 3*r_over)%mod
print(ans)

'''
愚直解を考える
3^Nで場合分けする

辺の長さをx<=y<=zとして、
三角形が存在する場合は、x+y>z

整数も300以下なのでそれを使いそう
dp[i][j] := x=i,y=j となる場合の数

→　x,yの合計が決められれば、あとは適当に分けるだけ？
　 違う。y<=zを守らないといけない。

s = sum(ai)
dp[i][j] := i個の辺を使って、合計jにできる場合の数
とすると、
Σ　dp[i][j (j <= ) ]

一辺の長さが決まってたとする。

？？？？
逆のパターンは？
三角形が作れない場合の数は？
x+y < z これだけ？？？
x=0
y=0
も。

3^N - 2^N*3 + 6 - ???

dp[i][j] := i個の辺を使って、合計jにできる場合の数
j >= n/2 について
sum(dp[i][(n+1)//2:]) * (i**2 -2)


1*1 + 2*301 + 3*601 + ... + n*(300n+1)

300(1*0 + 2*1 + 3*2 + 4*3 + ...) < 300(1*1 + 2*2 + ...)


dp[i][j] := i番目の数まで使って、Rの合計がjになる場合の数
として、GかBに突っ込んだ場合も数えておけばいいのでは。

i番目の数がaiのとき、
dp[i][j] = dp[i-1][j] * 2 + dp[i-1][j-ai]

あとは、どれかが0になるパターンを別で引けばいい

'''
