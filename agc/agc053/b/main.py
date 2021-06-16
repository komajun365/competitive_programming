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

n = int(input())
v = list(map(int,input().split()))

hq = []
for i in range(n):
    l = n-i-1
    r = n+i
    heappush(hq,v[l])
    if hq[0] < v[r]:
        heappop(hq)
        heappush(hq,v[r])

print(sum(hq))





'''
12563478

12756348
127634
1234

8734

12756348
[5],6
[6]
[6,7],10


6748

56123478



'''