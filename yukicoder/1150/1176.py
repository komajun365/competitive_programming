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

a = int(input())

ans = 200
for n in range(2,130):
    com = 1
    for m in range(1,100):
        com *= n
        if(com >= a):
            break
    ans = min(n*m,ans)
print(ans)
