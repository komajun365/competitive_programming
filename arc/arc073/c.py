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

N,T = map(int,input().split())
t = list(map(int,input().split()))

ans = 0
for i in range(1,N):
    ans += min(T,t[i]-t[i-1])

ans += T
print(ans)
