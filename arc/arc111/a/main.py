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

n,m = map(int,input().split())

if m==1:
    print(0)
    exit()

ans = dict()
next = dict()
# ans = [[-1] * m for _ in range(m)]
# next = [[-1] * m for _ in range(m)]

x = 0
y = 1
cnt = 0
while(not x*m+y in ans):
    ans[x*m+y] = cnt
    y1 = y*10 
    x1 = (10*x + y1//m)%m
    y1 %= m
    next[x*m+y] = x1*m+y1
    x,y = x1,y1
    if cnt == n:
        print(x)
        exit()
    cnt += 1

loop = cnt - ans[x*m+y]
base = ans[x*m+y]

for i in range(loop):
    if (n-base) % loop == i:
        print(x)
        exit()
    x,y = next[x*m+y] // m,next[x*m+y] % m




