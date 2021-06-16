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

a,b = input().split()
a = list(a)
b = list(b)

def calc(a,b):
    x,y = 0,0
    for ai in a:
        x = x*10 + int(ai)
    for bi in b:
        y = y*10 + int(bi)
    if x < 100 or y < 100:
        return -999
    else:
        return x-y

ans = -999
for i in range(3):
    for j in range(10):
        ax = a[::]
        bx = b[::]
        ax[i] = str(j)
        ans = max(ans, calc(ax,bx))
    for j in range(10):
        ax = a[::]
        bx = b[::]
        bx[i] = str(j)
        ans = max(ans, calc(ax,bx))
print(ans)


