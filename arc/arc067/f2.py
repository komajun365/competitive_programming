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

import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

n,m = map(int,readline().split())
a = list(map(int,readline().split()))
a += [0,0,0]
b = list(map(int,read().split()))

imos = [[] for _ in range(n+2)]
for i in range(n+2):
    imos[i] = [0] * (n+3-i)

for i in range(m):
    left = list(range(-1,n+1))
    right = list(range(1,n+3))

    bi = [(val,j) for j,val in enumerate(b[i::m], 1)]
    bi.sort()
    for val,j in bi:
        l = left[j]
        r = right[j]
        imos[l+1][j-l] += val
        imos[l+1][r-l] -= val
        imos[j+1][j-j] -= val
        imos[j+1][r-j] += val
        right[l] = r
        left[r] = l

for i in range(n+1):
    for j in range(1,n+3-i):
        imos[i][j] += imos[i][j-1]

for i in range(1,n+1):
    for j in range(n+3-i):
        imos[i][j] += imos[i-1][j+1]

ans = 0
for i in range(1,n+1):
    dif = 0
    for j in range(i,n+1):
        ans = max(ans,imos[i][j-i+1] - dif)
        dif += a[j-1]

print(ans)

# for i in imos:
#     print(i)




'''
i~jの焼き肉店に行くときのおいしさの最大値が知りたい




'''
