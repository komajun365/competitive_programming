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
read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines

t,*query = map(int,read().split())
mod = 10**9 + 7
it = iter(query)
ans = []
for n,a,b in zip(it,it,it):
    if(a>b):
        a,b = b,a
    red = pow(n-a+1,2,mod)
    blue = pow(n-b+1,2,mod)
    tmp = (red*blue)%mod

    tmp -= blue * pow(b-a+1,2,mod)
    tmp%=mod

    if(a>1)&(n>b):
        min_ab = b+1
        max_ab = min(n,a+b-1)
        r = n-min_ab+1
        l = n-max_ab+1
        tot = ((l+r)*(r-l+1)//2)%mod
        tmp -= tot*(n-b+1)*(b-a+1)*4
        tmp %= mod
        tmp -= (tot*tot*4)%mod
        tmp %= mod
        # print(red,blue,min_ab,max_ab,tot)

    ans.append(tmp)
    # print(red,blue)

print('\n'.join(map(str,ans)))
