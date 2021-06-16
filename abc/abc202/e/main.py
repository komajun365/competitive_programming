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
import bisect

n,*data = map(int,read().split())
p = data[:n-1]
q = data[n-1]
ud = data[n:]

links = [[] for _ in range(n)]
for i,pi in enumerate(p,1):
    pi -= 1
    links[pi].append(i)


stack = [0]
depth = [0] * n
deps = [[] for _ in range(n)]
et = []
while stack:
    i = stack.pop()
    if i < 0:
        i = ~i
        et.append(i)
    else:
        deps[depth[i]].append(len(et))
        et.append(i)
        stack.append(~i)
        for j in links[i]:
            stack.append(j)
            depth[j] = depth[i] + 1
            

idx = [[-1,-1] for _ in range(n)]
for i in range(n*2):
    ei = et[i]
    if idx[ei][0] == -1:
        idx[ei][0] = i
    else:
        idx[ei][1] = i

ans = []
it = iter(ud)
for u,d in zip(it,it):
    u -= 1
    if depth[u] > d:
        ans.append(0)
        continue

    left,right = idx[u]
    tmp = bisect.bisect_left(deps[d], right) - bisect.bisect_left(deps[d], left)
    ans.append(tmp)

    # print(u,d)
    # print(bisect.bisect_left(deps[d], left))
    # print(bisect.bisect_left(deps[d], right))

print('\n'.join(map(str,ans)))
