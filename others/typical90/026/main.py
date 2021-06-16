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

n,*ab = map(int,read().split())

links = [[] for _ in range(n)]
it = iter(ab)
for a,b in zip(it,it):
    a -= 1
    b -= 1
    links[a].append(b)
    links[b].append(a)

depth = [-1] * n
stack = [0]
depth[0] = 0
even = [0+1]
odd = []
while stack:
    i = stack.pop()
    for j in links[i]:
        if depth[j] != -1:
            continue
        depth[j] = depth[i] + 1
        if depth[j] % 2 == 0:
            even.append(j+1)
        else:
            odd.append(j+1)
        stack.append(j)

if len(even) >= n//2:
    ans = even[:n//2]
else:
    ans = odd[:n//2]
print(*ans, sep=' ')