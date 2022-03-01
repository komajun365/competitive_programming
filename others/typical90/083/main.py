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

n,m,*data = map(int,read().split())
ab = [x-1 for x in data[:2*m]]
q = data[2*m]
xy = data[2*m+1:]

deg = [0] * n
it = iter(ab)
for a,b in zip(it,it):
    deg[a] += 1
    deg[b] += 1

lim = int(m**0.5)
fast = [[] for _ in range(n)]
late = [[] for _ in range(n)]
it = iter(ab)
for a,b in zip(it,it):
    if deg[a] > lim:
        late[b].append(a)
    else:
        fast[a].append(b)
    if deg[b] > lim:
        late[a].append(b)
    else:
        fast[b].append(a)

ans = []
color = [1] * n
draw = [-1] * n
q_color = [-1] * n
query = [-1] * n

for i in range(q):
    x,y = xy[i*2:i*2+2]
    x -= 1
    for j in late[x]:
        if query[j] > draw[x]:
            color[x] = q_color[j]
            draw[x] = query[j]
    ans.append(color[x])
    
    color[x] = y
    draw[x] = i
    q_color[x] = y
    query[x] = i
    for j in fast[x]:
        color[j] = y
        draw[j] = i

print('\n'.join(map(str,ans)))

