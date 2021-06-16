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

n,m,k,*data = map(int,read().split())
h = data[:n]
c = data[n:n+k]
ab = data[n+k:]

links = [[] for _ in range(n)]
it = iter(ab)
for a,b in zip(it,it):
    a -= 1
    b -= 1
    if h[a] < h[b]:
        links[a].append(b)
    else:
        links[b].append(a)

ans = [-1] * n
for ci in c:
    ans[ci-1] = 0

stack = [ci-1 for ci in c]
while stack:
    stack2 = []
    while stack:
        i = stack.pop()
        for j in links[i]:
            if ans[j] != -1:
                continue
            ans[j] = ans[i] + 1
            stack2.append(j)
    stack,stack2 = stack2,stack

print('\n'.join(map(str,ans)))