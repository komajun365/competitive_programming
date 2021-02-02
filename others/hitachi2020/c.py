import sys
import os
f = open('../../input.txt', 'r')
sys.stdin = f

import sys
input = sys.stdin.readline

n = int(input())
ab = [list(map(int,input().split())) for _ in range(m)]

edges = {}
for i in range(1,n+1):
    edges[i] = []

n_num = [0] * (n+1)
for tmp in ab:
    a,b = tmp
    edges[a].append(b)
    edges[b].append(a)
    n_num[a] += 1
    n_num[b] += 1

start = 0
for i in range(1,n+1):
    if(n_num[i] == 1):
        start = i
        break
