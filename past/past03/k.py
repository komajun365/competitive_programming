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

n,q = map(int,readline().split())
data = list(map(int,read().split()))

parent = list(range(0,-(n+1),-1))
top = list(range(n+1))

for i in range(q):
    f,t,x = data[i*3:(i+1)*3]
    top[f],parent[x],top[t] = parent[x],top[t],top[f]

ans = [0] * (n+1)
for d,i in enumerate(top[1:],1):
    while(i>0):
        ans[i] = d
        i = parent[i]

print('\n'.join(map(str,ans[1:])))
