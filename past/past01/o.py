# a,b = map(int,input().split())
# a = list(map(int,input().split()))
# a = [list(map(int,input().split())) for _ in range(n)]

# 検討?分　実装分 バグとり分

import sys
import os
f = open('../../input.txt', 'r')
sys.stdin = f

import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

n = int(readline())
data = list(map(int,read().split()))
nums = sorted(list(set(data)))
dict_en = {}
for i,val in enumerate(nums,1):
    dict_en[val] = i

it = iter(data)
a = [ list(i) for i in zip(it,it,it,it,it,it)]
written = [-1] * (n*6+1)
for i in range(n):
    for j in range(6):
        num = dict_en[a[i][j]]
        a[i][j] = num
        written[num] = i

dp = [0] * (n*6+1)
dp[-1] = 1
dice = written[n*6]
for i in range(n*6-1,-1,-1):
    cand = written[i+1]
    cand_ex = 1
    for j in a[cand]:
        if(j>i):
            cand_ex += dp[j]/6
    if(cand_ex >= dp[i+1]):
        dp[i] = cand_ex
        dice = cand
    else:
        dp[i] = dp[i+1]

print(dp[0])
