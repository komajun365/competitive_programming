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

n,m,l = map(int,input().split())
pqr = list(map(int,input().split()))

ans = 0
for i,j,k in [[0,1,2], [0,2,1]]:
    for _ in range(3):
        tmp = (n//pqr[i]) * (m//pqr[j]) * (l//pqr[k])
        ans = max(ans,tmp)
        i,j,k = j,k,i

print(ans)    
