# a,b = map(int,input().split())
# a = list(map(int,input().split()))
# a = [list(map(int,input().split())) for _ in range(n)]

# 検討15分　実装分 バグとり分

import sys
import os
f = open('../../input.txt', 'r')
sys.stdin = f

import sys
input = sys.stdin.readline

n = int(input())
cost = [int(input()) for _ in range(n-1)]
cost.append(0)

inf = 10**5
def update(dp,s):
    len_ = min(s+1, (n-s)+1)
    res = [inf]* len_
    c_1,c_2 = cost[s-1],cost[s-2]
    if(s <= n//2):
        res[0] = cost[s-1]
        for i in range(1,len_-1):
            res[i] = min(dp[i] - c_2, dp[s-i-1]) + c_1
    else:
        for i in range(len_):
            res[i] = min(dp[i+1] - c_2, dp[len_-i-1]) + c_1
    return res

dp = [cost[0],inf]
for s in range(2,n+1):
    dp = update(dp,s)

print(dp[0])

'''
方針
dp
左から棒を切るor切らないを判断していく。
aさんがもらう領域をai、bさんがもらう領域をbiとすると、
切れ目ごとに領域をa1,b1,a2,b2,...としていって、
sum(ai)とsum（bi)がそれぞれn//2になればよい。
※交互に分割しない場合、例えばa1,b1,b2,a2,...となるような分割は、
　b1とb2の間で切る必要がない。なので適切な分割は必ず交互になる。

s=i+jまで切った時のことを考える。
i=最後に切った領域をもらう人がそこまでにもらった長さ合計、j=そうじゃないほうの領域の長さ合計として、
dp[i][j]に条件を満たすコストの最小値を格納する。
すると、
dp[i][j] = min(dp[j][i-x]) + cost[i+j]　(※1 <= x <= i)
で更新できるが、このままだと一回の更新にo(N)となり、全体でO(N**3)。

そこで、
dp[i-1][j] = min(dp[j][i-1-x]) + cost[i+j-1]　(※1 <= x <= i-1)
であることに着目すると、
dp[i][j] = min(dp[i-1][j] - cost[i+j-1], dp[j][i-1]) + cost[i+j]
で更新できる。これで一回の更新がo(1)となり、全体でO(N**2)にできた。

のだが、dp[i][j]はサイズがでかいのでメモリの節約が必要。
dp[i][j]の更新に見るのはdp[i-1][j]とdp[j][i-1]なので、
s(=i+j)でループを回すことにすれば、s-1の結果だけ残していけばOK。
（添え字がややこしいけどそこは気合で）

加えて、pypyで10**8オーダーはきついので定数倍高速化も気にしながらやる。
（i,jはn//2までしか見ない、など。）

'''

# n2 = n//2
#
# inf = 10**5
# dp = [[inf]*(1 + n2) for _ in range(1 + n2)]
#
# dp[0][0] = 0
# for i in range(1,n2+1):
#     dp[i][0] = cost[i-1]
#
# for s in range(2,n+1):
#     for i in range( max(1, s-n2) , min(s-1, n2)+1 ):
#         j = s-i
#         dp[i][j] = min(dp[i-1][j] - cost[i+j-2], dp[j][i-1]) + cost[i+j-1]
#
# print(dp[n2][n2])
