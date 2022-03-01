# oj t -c "python main.py" -d "./tests/" 

# a,b = map(int,input().split())
# a = list(map(int,input().split()))
# a = [list(map(int,input().split())) for _ in range(n)]

# import sys
# read = sys.stdin.buffer.read
# readline = sys.stdin.buffer.readline
# readlines = sys.stdin.buffer.readlines

# 検討?分　実装分 バグとり分

# import sys
# import os
# f = open('../../../input.txt', 'r')
# sys.stdin = f

import sys
read = sys.stdin.buffer.read

n,p,k,*a = map(int,read().split())

def warshall_floyd(d,n):
    #d[i][j]: iからjへの最短距離
    for k in range(n):
        for i in range(n):
            for j in range(n):
                d[i*n+j] = min(d[i*n+j],d[i*n+k] + d[k*n+j])
    return d

def calc(x):
    d = [ai if ai != -1 else x for ai in a]
    d = warshall_floyd(d,n)
    cnt = 0
    for i in range(n-1):
        for j in range(i+1,n):
            if d[i*n+j] <= p:
                cnt += 1
    return cnt

cnt = calc(10**9+1)
if cnt == k:
    print('Infinity')
    exit()

if cnt > k:
    print(0)
    exit()

def max_y(y):
    ok = 0
    ng = 10**9 + 1
    while ng-ok > 1:
        mid = (ok+ng) //2
        if calc(mid) >= y:
            ok = mid
        else:
            ng = mid
    return ok

ans = max_y(k) - max_y(k+1)
print(ans)

# print(max_y(k+1))
# print(max_y(k))

# print(calc(2))
# print(calc(3))
# print(calc(4))