# oj t -c "python main.py" -d "./tests/" 

# a,b = map(int,input().split())
# a = list(map(int,input().split()))
# a = [list(map(int,input().split())) for _ in range(n)]

# import sys
# read = sys.stdin.buffer.read
# readline = sys.stdin.buffer.readline
# readlines = sys.stdin.buffer.readlines

# 検討?分　実装分 バグとり分

# import sys
# import os
# f = open('../../../input.txt', 'r')
# sys.stdin = f

import sys
read = sys.stdin.buffer.read

n,q,*data = map(int,read().split())
ab = data[:(n-1)*2]
cd = data[(n-1)*2:]

links = [[] for _ in range(n)]
it = iter(ab)
for a,b in zip(it,it):
    a -= 1
    b -= 1
    links[a].append(b)
    links[b].append(a)

depth = [-1] * n
depth[0] = 0
stack = [0]
while stack:
    i = stack.pop()
    for j in links[i]:
        if depth[j] != -1:
            continue
        depth[j] = depth[i] + 1
        stack.append(j)

ans = []
it = iter(cd)
for c,d in zip(it,it):
    c -= 1
    d -= 1
    if (depth[c] + depth[d]) % 2 == 0:
        ans.append('Town')
    else:
        ans.append('Road')
print('\n'.join(ans))