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

from heapq import heappop,heappush

n,m = map(int,input().split())
a = list(map(int,input().split()))

hq = []
for ai in a:
    heappush(hq,ai*-1)

for _ in range(m):
    i = heappop(hq)*-1
    i //= 2
    heappush(hq,i*-1)

ans = sum(hq) * -1
print(ans)