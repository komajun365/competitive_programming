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

tot = sum(a)
ans = -1
dif = 10**6
for i,ai in enumerate(a):
    dif_i = abs(ai*n - tot)
    if(dif > dif_i):
        dif = dif_i
        ans = i
print(ans)
