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

n,*ab = map(int,read().split())
cnt = [0] * 400001
idx = [set() for _ in range(400001)]
for i,x in enumerate(ab):
    cnt[x] += 1
    idx[x].add(i)

stack = []
for i in range(400001):
    if cnt[i] == 1:
        stack.append(i)

ans = 0
while(stack):
    i = stack.pop()
    if cnt[i] == 0:
        continue
    i_idx = idx[i].pop()
    cnt[i] -= 1

    if i_idx%2==0:
        j_idx = i_idx+1
    else:
        j_idx = i_idx-1
    j = ab[j_idx]

    idx[j].remove(j_idx)
    cnt[j] -= 1
    if cnt[j] == 1:
        stack.append(j)
    ans += 1

rem = 0
for i in range(400001):
    if cnt[i] > 0:
        rem += 1
rem = min(rem, n-ans)
ans += rem
print(ans)





