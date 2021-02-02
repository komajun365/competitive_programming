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

for i in range(n):
    for k in range(n):
        if(a[i-1][k] == 0):
            continue
        for j in pair_dic[i]:
            if(  ((j&(1<<k)) >>k == 0 ) ):
                dp[j + (1<<k)] += dp[j]
                dp[j + (1<<k)] = dp[j + (1<<k)] % MOD

print(dp[-1])



[1] + [3] + [5]

[1,3,5] + [7]


N = 5
bit_count = [0]
for _ in range(N):
    bit_count += [x+1 for x in bit_count]
bit_count
