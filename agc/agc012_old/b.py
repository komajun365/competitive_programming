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
data = list(map(int,read().split()))
ab = data[:2*m]
q = data[2*m]
vdc = data[2*m+1:]

links = [[] for _ in range(n+1)]
it = iter(ab)
for a,b in zip(it,it):
    links[a].append(b)
    links[b].append(a)

ans = [0] * (n+1)
length = [-1] * (n+1)

for i in range(q-1,-1,-1):
    v,d,c = vdc[i*3:i*3+3]
    if( length[v] >= d):
        continue
    length[v] = d

    stack = [(v,d)]
    while(stack):
        vj,dj = stack.pop()
        if(ans[vj]==0):
            ans[vj] = c
        if(dj > 0):
            for vk in links[vj]:
                if( length[vk] < dj-1):
                    stack.append((vk,dj-1))
                    length[vk] = dj-1

print('\n'.join(map(str,ans[1:])))
