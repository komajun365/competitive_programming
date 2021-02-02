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

n,m,k = map(int,input().split())
a = list(map(int,input().split()))
b = list(map(int,input().split()))

a_tot = [0] * (n+1)
b_tot = [0] * (m+1)

for i,ai in enumerate(a,1):
    a_tot[i] = a_tot[i-1] + ai

for i,bi in enumerate(b,1):
    b_tot[i] = b_tot[i-1] + bi

# print(a_tot)

b_num = m
ans = 0
for a_num in range(n+1):
    rem = k - a_tot[a_num]
    if(rem < 0):
        break
    if(b_num==0):
        ans = max(ans,a_num)
    else:
        while(b_tot[b_num] > rem):
            b_num -= 1
        ans = max(ans,a_num+b_num)

print(ans)
