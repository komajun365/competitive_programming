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
a = list(map(int,input().split()))

cnt = [0,0]
for i,x in zip([0,1],[1,-1]):
    now = 0
    for aj in a:
        now += aj
        if(now == 0):
            cnt[i] += 1
            now = x
        elif( now * x < 0):
            cnt[i] += abs(now - x)
            now = x
        x *= -1

print(min(cnt))