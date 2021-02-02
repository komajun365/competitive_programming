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

n = int(readline())
uv = list(map(int,read().split()))

it = iter(uv)
links = [[] for _ in range(n+1)]
for u,v in zip(it,it):
    links[v].append(u)
    links[u].append(v)

ans = 0
tmp = 0
for i in range(1,n+1):
    tmp += i
    for j in links[i]:
        if(j<i):
            tmp -= j
    ans += tmp

print(ans)



'''
根を決めて、どこかの頂点から
1-iまでの連結成分　→countできる

ある連結成分が

'''
