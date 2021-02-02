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
a,b = map(int,input().split())
p = list(map(int,input().split()))

cnt = [0] * 3
for pi in p:
    if(pi <= a):
        cnt[0] += 1
    elif(pi > b):
        cnt[2] += 1
    else:
        cnt[1] += 1

print(min(cnt))
