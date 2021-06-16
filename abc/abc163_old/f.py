# a,b = map(int,input().split())
# a = list(map(int,input().split()))
# a = [list(map(int,input().split())) for _ in range(n)]

import sys
import os
f = open('../../input.txt', 'r')
sys.stdin = f

import sys
input = sys.stdin.readline

n = int(input())
c = list(map(int,input().split()))
links = [[] for _ in range(n+1)]
for _ in range(n-1):
    a,b = map(int, input().split())
    links[a].append((c,b))
    links[b].append((c,a))

sum = [0] * (n+1)
tmp = [0] * (n+1)
