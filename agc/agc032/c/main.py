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
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

n,m,*ab = map(int,read().split())
cnt = [0] * (n+1)
for x in ab:
    cnt[x] += 1
for ci in cnt:
    if ci % 2 == 1:
        print('No')
        exit()

if(max(cnt) >= 6):
    print('Yes')
    exit()
if(sum(cnt) >= 2*n + 6):
    print('Yes')
    exit()

cir = 0
it = iter(ab)
links = [set() for _ in range(n)]
for a,b in zip(it,it):
    a -= 1
    b -= 1
    if(b in links[a]):
        links[a].remove(b)
        links[b].remove(a)
        cir += 1
    elif(a == b):
        cir += 1
    else:
        links[a].add(b)
        links[b].add(a)

while(cir < 3):
    head = -1
    for i in range(n):
        if links[i]:
            head = i
            break
    else:
        print('No')
        exit()
    
    go = [0] * n
    go[head] = 1
    route = [head]
    x = head
    while(links[x]):
        y = links[x].pop()
        links[y].remove(x)
        x = y
        if x == head:
            cir += 1
            break
        if go[x] == 1:
            cir += 1
            tail = x
            while(route[-1] != tail):
                tmp = route.pop()
                go[tmp] -= 1
            continue
        go[x] += 1
        route.append(x)

print('Yes')