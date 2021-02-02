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

ans = 0
for i in range(100,1000):
    for j in range(100,1000):
        s = str(i*j)
        if(s == s[::-1]):
            ans = max(ans, i*j)

print(ans)
