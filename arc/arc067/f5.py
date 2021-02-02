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
a = tuple(a)
b = tuple(map(int,read().split()))

ans = 0
imos = [[0] * (n+2) for _ in range(2)]
query = [dict() for _ in range(n+2)]
for i in range(n-1):
    imos[0][i+2] -= a[i]
    if(i+2 in query[i+2]):
        query[i+2][i+2] += a[i]
    else:
        query[i+2][i+2] = a[i]
for i in range(n+1):
    imos[0][i+1] += imos[0][i]

bi = [0] * n

for i in range(m):
    left = list(range(-1,n+1))
    right = list(range(1,n+3))

    for j,val in enumerate(b[i::m], 1):
        bi[j-1] = (val,j)
    bi.sort()

    for val,j in bi:
        l = left[j]
        r = right[j]
        for x,y,val2 in zip([l+1,l+1,j+1,j+1],[j,r,j,r],[val,-val,-val,val]):
            if(y in query[x]):
                query[x][y] += val2
            else:
                query[x][y] = val2
        right[l] = r
        left[r] = l

for i in range(1,n+1):
    i0 = 1-(i%2)
    i1 = i%2
    for j in range(0,n+1):
        imos[i1][j] = 0
    for qi,val in query[i].items():
        imos[i1][qi] += val
    for j in range(i,n+1):
        imos[i1][j] += imos[i1][j-1]
    for j in range(i,n+1):
        imos[i1][j] += imos[i0][j]
        ans = max(ans,imos[i1][j])

print(ans)

for i in imos:
    print(i)
