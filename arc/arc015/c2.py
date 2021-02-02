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
from math import gcd

n = int(readline())
unit = set()
rate = dict()
for _ in range(n):
    large,m,small = readline().split()
    m = int(m)

    unit.add(large)
    unit.add(small)
    if(not large in rate):
        rate[large] = dict()
    if(not small in rate):
        rate[small] = dict()

    rate[large][small] = (m,1)
    rate[small][large] = (1,m)

ans = ['hoge',0,'hoge']
for i in unit:
    stack = [(1,1,i)]
    done = set()
    done.add(i)
    while(stack):
        cj,pj,j = stack.pop()
        if(pj==1)&(cj > ans[1]):
            ans = [i,cj,j]
        for k,(ck,pk) in rate[j].items():
            if(k in done):
                continue

            c,p = cj*ck,pj*pk
            gcd_num = gcd(c,p)
            c,p = c//gcd_num,p//gcd_num

            stack.append((c,p,k))
            done.add(k)

print('1{}={}{}'.format(*ans))
if(ans[1]==1):
    print('hoge')
