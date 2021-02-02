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

s = input()
alp = set(s)
rem = 0
odd = 0
for si in alp:
    cnt = s.count(si)
    odd += cnt%2
    rem += cnt//2
if(odd==0):
    ans = len(s)
else:
    ans = 1 + (rem//odd)*2
print(ans)
