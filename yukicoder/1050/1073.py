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

from fractions import Fraction

n = int(input())

num_1_6 = Fraction(1,6)

dp = []
dp.append(Fraction(1,1))
for i in range(1,30):
    tmp = dp[i-1] * num_1_6
    if(i>1):
        tmp += dp[i-2] * num_1_6
    if(i>2):
        tmp += dp[i-3] * num_1_6
    if(i>3):
        tmp += dp[i-4] * num_1_6
    if(i>4):
        tmp += dp[i-5] * num_1_6
    if(i>5):
        tmp += dp[i-6] * num_1_6
    dp.append(tmp)

for i in dp:
    print(i)


'''
1
1/6
7/36




'''
