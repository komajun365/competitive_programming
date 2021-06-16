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

k = int(input())
x,y = map(int,input().split())

pmx = 1
pmy = 1
if x < 0:
    pmx = -1
    x *= -1
if y < 0:
    pmy = -1
    y *= -1

d = x+y
if d % 2 == 1 and k % 2 == 0:
    print(-1)
    exit()

def move(x0,y0,x1,y1):
    res = []
    while x0 + k <= x1:
        x0 += k
        res.append([x0,y0])
    dx = x1-x0
    dy = k - dx
    x0 += dx
    y0 += dy
    res.append([x0,y0])
    while y0 + k <= y1:
        y0 += k
        res.append([x0,y0])

ans = []
if d % k == 0:
    ans += move(0,0,x,y)
else:
    add = k - d%k
    if add % 2 == 1:
        add += k
    a = -1 * add //2
    b = k + a
    if x >= b:
        ans.append([b,a])
        ans += move(b,a,x,y)
    elif y >= b:
        ans.append([a,b])
        ans += move(a,b,x,y)
    else:
        





# ans = []
# if d % k != 0:
#     rem = d%k
#     if k % 2 == rem % 2:
#         a = (k+rem)//2
#         b = (k-rem)//2
#         if x >=a and y >= b:
#             ans.append([a,b])
#             x += a
#             y += b
#         elif x >= b and y >= a:
#             ans.append([b,a])
#             x += b
#             y += a
#         else:
#             add = k - rem

