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
c = [int(input()) for _ in range(n)]

ans = 0
for ci in c:
    num = 0
    for cj in c:
        num += (ci%cj==0)
    ans += ((num+1)//2)/num

print(ans)
