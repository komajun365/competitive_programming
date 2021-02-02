# a,b = map(int,input().split())
# a = list(map(int,input().split()))
# a = [list(map(int,input().split())) for _ in range(n)]

import sys
import os
f = open('../../input.txt', 'r')
sys.stdin = f

import itertools
n,m,q = map(int,input().split())
abcd = [tuple(map(int,input().split())) for _ in range(q)]

l = set(range(1,m+1))
h = itertools.combinations_with_replacement(l, n)

ans = 0
for i in h:
    tmp = 0
    for (a,b,c,d) in abcd:
        if(i[b-1]-i[a-1] == c):
            tmp += d
    ans = max(ans,tmp)

print(ans)
