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

x,y,n,*xy = map(int,read().split())

ans = 10000
def calc_dif(x0,y0,x1,y1):
    if x0 == x1:
        dif = abs(x0-x)
        dx = x0
        dy = y
    elif y0 == y1:
        dif = abs(y0-y)
        dx = x
        dy = y0
    else:
        a = 1
        b = -(x1-x0)/(y1-y0)
        c = - (x0 + b*y0)
        dif = abs(a*x + b*y + c) / (a**2 + b**2)**0.5

    return dif

xy += xy

for i in range(n):
    x0,y0 = xy[i*2:i*2+2]
    x1,y1 = xy[i*2+2:i*2+4]

    dif = calc_dif(x0,y0,x1,y1)
    ans = min(ans,dif)

print(ans)

