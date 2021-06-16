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

def dfs(root):
    ans = [-1] * n
    stack = [root]
    parent = [-1] * n
    dep = [-1] * n
    dep[root] = 0
    num = 0
    while stack:
        i = stack.pop()
        num += 1
        if i >= 0:
            ans[i] = num
            stack.append(~i)
            for j in links[i]:
                if dep[j] != -1:
                    continue
                dep[j] = dep[i] + 1
                parent[j] = i
                stack.append(j)
        else:
            i = ~i
    
    return dep,ans,parent

dep,_,_ = dfs(0)
max_dep = max(dep)
for i in range(n):
    if dep[i] == max_dep:
        break

dep,_,parent = dfs(i)
max_dep = max(dep)
for j in range(n):
    if dep[j] == max_dep:
        break

route = set()
x = j
while x != i:
    route.add(x)
    x = parent[x]

for j in range(n):
    links[j].sort(key = lambda x: 0 if x in route else 1)

_,ans,_ = dfs(i)

print(' '.join(map(str,ans)))
# print(tp)

