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

n,m,q = map(int,readline().split())
data = list(map(int,read().split()))
uv = data[:2*m]
c = [0] + data[2*m:2*m+n]
s = data[2*m+n:]

links = [[] for _ in range(n+1)]
it = iter(uv)
for u,v in zip(it,it):
    links[u].append(v)
    links[v].append(u)

ans = []
i = 0
max_i = len(s)
while(i < max_i):
    if(s[i]==1):
        x = s[i+1]
        i += 2

        ans.append(c[x])
        for neigh in links[x]:
            c[neigh] = c[x]
    else:
        x = s[i+1]
        y = s[i+2]
        i += 3

        ans.append(c[x])
        c[x] = y
        
print('\n'.join(map(str,ans)))
