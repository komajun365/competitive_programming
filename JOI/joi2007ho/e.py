# a,b = map(int,input().split())
# a = list(map(int,input().split()))
# a = [list(map(int,input().split())) for _ in range(n)]

import sys
import os
f = open('../../input.txt', 'r')
sys.stdin = f

from collections import deque
# 最大公約数
from fractions import gcd

n = int(input())
parent = [[0,0] for _ in range(n+1)]
child = [[0,0] for _ in range(n+1)]
child_w = [[1,1] for _ in range(n+1)]
lr = [[0,0] for _ in range(n+1)]

for i in range(1,n+1):
    l,r,cl,cr = map(int,input().split())
    parent[cl] = [i,0]
    parent[cr] = [i,1]
    child[i] = [cl,cr]
    lr[i] = [l,r]

for i,val in enumerate(parent[1:],1):
    if(val[0] == 0):
        root = i
        break

stack = []
d = deque()
d.append(root)
while(d):
    tmp = d.popleft()
    stack.append(tmp)
    for i in child[tmp]:
        if(i != 0):
            d.append(i)

for i in stack[::-1]:
    l,r = lr[i]
    wl,wr = child_w[i]
    balance = l*wl*r*wr//gcd(l*wl,r*wr)
    p,side = parent[i]
    child_w[p][side] = balance//l + balance//r

print(child_w[0][0])
