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

n,m,*data = map(int,read().split())
if m==0:
    exit()

ab0 = data[:2*m]
it = iter(ab0)
ab = [[a-1,b-1] for a,b in zip(it,it)]
c = data[2*m:]

deg = [0] * n
links = [set() for _ in range(n)]
for i in range(m):
    a,b = ab[i]
    links[a].add([b,i])
    links[b].add([a,i])
    deg[a] += 1
    deg[b] += 1

# hq = []
# for i,ci in enumerate(c):
#     heappush(hq, ci * n + i)

ans = [-1] * m
done = [0] * m
def cut_c1():
    cut = 0
    stack = []
    for i,ci in enumerate(c):
        if ci == 1:
            stack.append(i)
    
    while(stack):
        i = stack.pop()
        c[i] -= 1
        while(links[i])]
            j, m_idx = links[i].pop()
            if ab[m_idx][0] == i:
                ans[m_idx] = 0
            else:
                ans[m_idx] = 1
            c[j] -= 1
            links[c].remove([i,m_idx])
            if c[j] == 1:
                stack.append(j)
            deg[i] -= 1
            deg[j] -= 1


cut_c1()

check


