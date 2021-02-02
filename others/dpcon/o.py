import sys
import os
f = open('../../input.txt', 'r')
sys.stdin = f

n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]

MOD = 10**9 +7
dp = [0] * (1<<n)

pair_dic = {}
for i in range(n+1):
    pair_dic[i] = []

for i in range(1<<n):
    pair_dic[ bin(i).count('1') ].append(i)

dp[0] = 1
# for i in range(n):
#     for j in pair_dic[i]:
#         for k in range(n):
for i in range(n):
    for k in range(n):
        for j in pair_dic[i]:
            if( (a[i][k] == 1) & ( ((j&(1<<k)) >>k == 0 ) )):
                dp[j + (1<<k)] += dp[j]
                dp[j + (1<<k)] = dp[j + (1<<k)] % MOD


print(dp[-1])
