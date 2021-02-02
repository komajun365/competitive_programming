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

a,b,c = map(int,input().split())
ans = 100000
for i in range(-10,60):
    cnt = 0
    for x in [a,b,c]:
        while(x < i):
            x += 2
            cnt += 1
        cnt += x-i
    ans = min(ans,cnt)
print(ans)
