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
lr = list(map(int,read().split()))

imos = [0] * (m+2)
ans = [0] * (m+2)

it = iter(lr)
for l,r in zip(it,it):
    i = 1
    li = r+1
    while(li > i):
        ri = min(li, r//i + 1)
        li = (l-1)//i + 1
        if(ri > li):
            imos[li] += 1
            imos[ri] -= 1
        i+=1

    for i in range(1,li):
        if(r//i)-((l-1)//i)>0:
            ans[i] += 1

for i in range(1,m+1):
    imos[i] += imos[i-1]
    ans[i] += imos[i]

print('\n'.join(map(str,ans[1:m+1])))




'''
l-rで買える名産品
r//d == (l-1)//d だと買えない

r = l-1 + k
l-1 = ad + b
r = ad + b+k

b+k >= dなら買える






'''
