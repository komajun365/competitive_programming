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
a = list(map(int,input().split()))
b = list(map(int,input().split()))
c = list(map(int,input().split()))

for i in range(n):
    if(a[i]==0)&(b[i]==0)&(c[i]>0):
        print(-1)
        exit()

ok = 10**12 + 10
ng = -1

for _ in range(100):
    mid = (ok+ng)//2
    b_time = 0
    for ai,bi,ci in zip(a,b,c):
        tmp = (ci-ai*mid)
        if(tmp <= 0):
            continue

        if(bi==0):
            b_time = 10**8
            break

        tmp = (tmp-1)//bi + 1
        b_time += max(tmp,0)

    if(b_time <= mid):
        ok = mid
    else:
        ng = mid

print(ok)
