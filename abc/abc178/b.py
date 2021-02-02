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

a,b,c,d = map(int,input().split())
c1 = [a,b]
c2 = [c,d]
if(a <= 0 <= b):
    c1.append(0)
if(c <= 0 <= d):
    c2.append(0)

ans = -1 * 10**20
for x in c1:
    for y in c2:
        ans = max(ans,x*y)
print(ans)
