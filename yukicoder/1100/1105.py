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

# for k in range(100):
#     print(k,5**k)
#     if(5**k > 10**18):
#         break
#
# print(5**26)
# print(5**13)

n = int(input())
m = 27

base = [2] * m
lim_up = [2] * m
# lim_down = [2] * m
x = n
for i in range(m):
    x += 2
    lim_up[i] = x%5
    # lim_down[i] = 4 - lim_up[i]
    x //= 5

lim_up = lim_up[::-1]

# dp[i][j] *= i桁目まで見て、各桁の合計数がjのやつの個数
dp_0 = [[0]*(m*4+1) for _ in range(m+1)]
dp = [[0]*(m*4+1) for _ in range(m+1)]
dp_lim = [[0]*(m*4+1) for _ in range(m+1)]

dp_0[0][0] = 1
dp_lim[0][0] = 1

phase = 0
for i in range(1,m+1):
    dp_0[i][i*2] = 1
    lim_j = sum(lim_up[:i])
    dp_lim[i][lim_j] = 1
    if(lim_j != i*2)&(phase==0):
        phase = 1

    for j in range(m*4+1):
        dp[i][j] = sum(dp[i-1][max(0,j-4):j+1])
        if(phase==1):
            for k in range(3,lim_up[i-1]):
                dp[i][j] += dp_lim[i-1][j-k]
        elif(phase==2):
            for k in range(lim_up[i-1]):
                dp[i][j] += dp_lim[i-1][j-k]
            for k in range(3,5):
                dp[i][j] += dp_0[i-1][j-k]

    if(lim_j != i*2)&(phase==1):
        phase = 2

ans = dp[i][2*m] + dp_lim[i][2*m]
print(ans)

# for i in dp[-3:]:
#     print(i[42:52],i[52],i[53:62])

'''
左右に一個づつ分銅を置く。

同じ重さのものを置く意味はないので、
置いた分銅の重さを5^i,5^j (i<j)とすると
すると、そこで生じる重さの差は、
5^j-5^i = 5^i * (5^(j-i) - 1)

分銅が2m個あったとして、
1種類の錘の置き方は
(0,0),(1,0),(2,0),(0,1),(0,2)の5種類。

最大で26種類の錘を使いそう。
というわけで雑にやると5**26

左に乗せたり、右に乗せたりするのは面倒です。

左に２個ずつ分銅が乗っていて、
右に4つまで載せられるとしましょう。
左右の個数の一致条件は、右に乗せる分銅の合計数が2m個の時です。

5進数で、各桁の合計値が2mになっているものが作れる。

m = 26 として、
組み合わせパターン数は、

桁DPですね。。。

'''
