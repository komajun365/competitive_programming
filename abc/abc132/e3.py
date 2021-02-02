import sys
import os
f = open('../../input.txt', 'r')
sys.stdin = f

n, m = map(int, input().split())
uv = [list(map(int, input().split())) for _ in range(m)]
s, t = map(int, input().split())

next_dict = {}

for i in range(1,n*3 + 1):
    next_dict[i] = []

for i in range(m):
    u,v = uv[i]
    for j in range(3):
        next_dict[u + (j * n)].append((v + ((j+1)%3 * n )))

from collections import deque
d = deque()
d.append(s)

length = [-1] * (3*n + 1)
length[s] = 0

while(True):
    if(len(d) == 0):
        break

    num = d.popleft()
    for i in next_dict[num]:
        if( length[i] == -1 ):
            d.append(i)
            length[i] = length[num] + 1

    if(length[t] != -1):
        break

print(length[t] // 3)
