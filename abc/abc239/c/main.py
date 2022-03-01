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

x1,y1,x2,y2 = map(int,input().split())
for dx,dy in zip([-1,-1,1,1,-2,-2,2,2],[-2,2,-2,2,-1,1,-1,1]):
    x = x1 + dx
    y = y1 + dy
    if (x-x2)**2 + (y-y2)**2 == 5:
        print('Yes')
        exit()
print('No')