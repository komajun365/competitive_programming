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

n,k = map(int,input().split())
a = list(map(int,input().split()))

a0 = a[:n-k]
a1 = a[k:]

ans = []

for x,y in zip(a0,a1):
    if(x<y):
        ans.append('Yes')
    else:
        ans.append('No')

print('\n'.join(ans))
