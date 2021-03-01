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
from heapq import heappop,heappush

n,m,x,y,*abtk = map(int,read().split())

links = [[] for _ in range(n+1)]
it = iter(abtk)
for a,b,t,k in zip(it,it,it,it):
    links[a].append([b,t,k])
    links[b].append([a,t,k])

inf = 10**16
base = 1 << 20
d = [inf] * (n+1)
hq = []
heappush(hq, x)
while(hq):
    # print(d)
    num = heappop(hq)
    time,i = divmod(num,base)
    # print(time,i)
    if d[i] != inf:
        continue
    d[i] = time
    if i==y:
        print(time)
        exit()
    for j,t,k in links[i]:
        if d[j] != inf:
            continue
        start = -((-1*time) // k) * k
        # print(start,t,j)
        heappush(hq, ( (start+t)*base + j))
    
print(-1)

# print(links)
