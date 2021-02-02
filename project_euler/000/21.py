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
f = open('p018_triangle.txt', 'r')
sys.stdin = f

n = 10000
tot = [0] * n
for i in range(1,n):
    for j in range(i*2,n,i):
        tot[j] += i

# print(tot[:20])

ans = 0
for i in range(1,n):
    j = tot[i]
    if(i==j)|(j >= n):
        continue
    if(tot[j]==i):
        ans += i

print(ans)

'''
O(NlogN)ぐらいで全探索できます

'''
