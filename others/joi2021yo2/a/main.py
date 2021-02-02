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

from heapq import heappush,heappop

n,a = map(int,input().split())
s = input()

lr = [[0],[n+1]]
for i,si in enumerate(s,1):
    if(si=='#'):
        if(i < a):
            heappush(lr[0], i*-1)
        else:
            heappush(lr[1], i)

d = 1
now = a
ans = 0
while(lr[0][0] != 0) or (lr[1][0] != n+1):
    x = heappop(lr[d])
    if(d==0):
        x *= -1
    ans += abs(now - x)
    now = x
    if(x == 0) or (x == n+1):
        heappush(lr[d],x)
    d = 1-d

print(ans)
    

