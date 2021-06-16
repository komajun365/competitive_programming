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

a,b = map(int,input().split())

night = set([1,2,3,4,5,23,24,25,26,27,28,29,47,48])

ans = 0
for i in range(a+1,b+1):
    if(i in night):
        ans += 1

print(ans)
