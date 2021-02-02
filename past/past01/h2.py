# a,b = map(int,input().split())
# a = list(map(int,input().split()))
# a = [list(map(int,input().split())) for _ in range(n)]

# 検討?分　実装分 バグとり分

import sys
import os
f = open('../../input.txt', 'r')
sys.stdin = f

import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

n = int(readline())
c = list(map(int, readline().split()))
q = int(readline())
ss = [tuple(map(int,i.split())) for i in readlines()]

len_odd = (n+1)//2
len_even = n//2

# [odd,even]
if(n>1):
    min_c = [min(c[::2]),min(c[1::2])]
else:
    min_c = [c[0],10**10]
minus = [0,0]

ans = 0
for s in ss:
    if(s[0]==1):
        x,a = s[1:]
        x -= 1
        if(c[x] - minus[x%2] >= a):
            ans += a
            c[x] -= a
            min_c[x%2] = min(min_c[x%2], c[x])
    elif(s[0]==2):
        a = s[1]
        if(min_c[0] - minus[0] >= a):
            ans += a*len_odd
            minus[0] += a
    elif(s[0]==3):
        a = s[1]
        if(min_c[0] - minus[0] >= a)&(min_c[1] - minus[1] >= a):
            ans += a*n
            minus[0] += a
            minus[1] += a

print(ans)
