# a,b = map(int,input().split())
# a = list(map(int,input().split()))
# a = [list(map(int,input().split())) for _ in range(n)]

# import sys
# read = sys.stdin.buffer.read
# readline = sys.stdin.buffer.readline
# readlines = sys.stdin.buffer.readlines

# 検討9分　実装25分 バグとり6分

import sys
import os
f = open('../../input.txt', 'r')
sys.stdin = f

import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

n,m = map(int, readline().split())
a = map(int, read().split())

cumsum = [[0] * (n+1) for _ in range(m+1)]
for i,num in enumerate(a):
    for j in range(1,m+1):
        cumsum[j][i+1] = cumsum[j][i]
    cumsum[num][i+1] += 1

max_b = 2**m
num = [-1] * (max_b)
inf = n*2
dp = [inf] * (max_b)
num[0] = 0
dp[0] = 0

for i in range(1,max_b):
    for j in range(m):
        if(i>>j & 1):
            if(num[i] == -1):
                num[i] = num[i^(1<<j)] + cumsum[j+1][-1]
            dp[i] = min(dp[i], dp[i^(1<<j)] + num[1<<j] - (cumsum[j+1][num[i]] - cumsum[j+1][num[i^(1<<j)]]))

print(dp[-1])



'''
方針
bitDP
ぬいぐるみを一つとって、どれでも好きな種類のぬいぐるみに入れ替えられるとする。
最終的に各種類のぬいぐるみ数が変化しなければ、そうしても取り出すぬいぐるみの数は変わらない。
dp[i]前からi(bit)に対応するぬいぐるみを配置済みの取り出すぬいぐるみ最小数
とすればよい。

あらかじめ、i種類のぬいぐるみ総数をnum[i]
i種類目のぬいぐるみがj番目までに出現した回数をcumsum[i][j]
として求めておけば下記で更新できる。

for b in range(m):
    if(i>>b & 1)&(j!=b):
        dp[i][j] = min(dp[i][j], dp[i^(1<<b)][b] + num[j] - (cumsum[sum] - ))

累積和の算出がO(NM)
DPの更新がO(M^2 * 2^M)

'''
