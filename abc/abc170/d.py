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
a.sort()

n_max = 10**6+1

ans = 0
flag = [True] * (n_max)
for i in range(n-1):
    if(not flag[a[i]]):
        continue

    if(a[i]!=a[i+1]):
        ans += 1
    for j in range(a[i],n_max,a[i]):
        flag[j] = False

ans += flag[a[-1]]*1
print(ans)
