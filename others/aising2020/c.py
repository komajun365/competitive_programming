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
ans = [0] * (n+1)
for x in range(1,101):
    for y in range(1,101):
        for z in range(1,101):
            tmp = x**2+y**2+z**2+x*y+y*z+z*x
            if(tmp<=n):
                ans[tmp] += 1

print('\n'.join(map(str,ans[1:])))
