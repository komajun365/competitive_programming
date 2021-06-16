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

n,*data = map(int,read().split())
it = iter(data)
xy = [[x,y] for x,y in zip(it,it)]

x_min = [10**10,-1]
x_max = [-1*10**10,-1]
y_min = [10**10,-1]
y_max = [-1*10**10,-1]
for i in range(n):
    x,y = xy[i]
    if x_min[0] > x:
        x_min = [x,i]
    if x_max[0] < x:
        x_max = [x,i]
    if y_min[0] > y:
        y_min = [y,i]
    if y_max[0] < y:
        y_max = [y,i]

xs = [x_min[1], x_max[1]]
xs.sort()
ys = [y_min[1], y_max[1]]
ys.sort()
x = data[::2]
y = data[1::2]
x.sort()
y.sort()

if xs == ys:
    ans = max(x[-1] - x[1], x[-2] - x[0], 
                y[-1] - y[1], y[-2] - y[0])
elif x_max[0] - x_min[0] == y_max[0] - y_min[0]:
    ans = x_max[0] - x_min[0]
elif x_max[0] - x_min[0] > y_max[0] - y_min[0]:
    ans = max(y_max[0] - y_min[0],
                x[-1] - x[1], x[-2] - x[0])
else:
    ans = max(x_max[0] - x_min[0],
                y[-1] - y[1], y[-2] - y[0])
print(ans)
