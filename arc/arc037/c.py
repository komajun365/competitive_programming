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
b = list(map(int,input().split()))
a.sort()
b.sort()

def rank(x):
    res = 0
    i = n
    for j in range(n):
        while(i > 0):
            if(a[i-1] * b[j] > x):
                i -= 1
            else:
                break
        res += i
    return res

ok = 0
ng = 10**18
while(ng-ok > 1):
    mid = (ok+ng)//2
    rank_mid = rank(mid)
    if(rank_mid < k):
        ok = mid
    else:
        ng = mid

print(ng)
