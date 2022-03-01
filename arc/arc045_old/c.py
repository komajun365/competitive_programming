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
from collections import defaultdict

n,X = map(int,readline().split())
xyc = list(map(int,read().split()))


links = [[] for _ in range(n+1)]
it = iter(xyc)
for x,y,c in zip(it,it,it):
    links[x].append((c,y))
    links[y].append((c,x))

num = [-1] * (n+1)
num[1] = 0
stack = [1]
while(stack):
    i = stack.pop()
    for c,j in links[i]:
        if(num[j] != -1):
            continue
        num[j] = num[i] ^ c
        stack.append(j)

d = defaultdict(int)
ans = 0
for i,num_i in enumerate(num[1:],1):
    ans += d[num_i^X]
    d[num_i] += 1

print(ans)
