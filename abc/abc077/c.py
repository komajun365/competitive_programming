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

a.sort()
b.sort()
c.sort()

ans = 0
i,k = 0,0
for j in range(n):
    bj = b[j]
    while(i<n):
        if(a[i] >= bj):
            break
        i += 1
    while(k<n):
        if(c[k] > bj):
            break
        k += 1
    ans += i * (n-k)

print(ans)
