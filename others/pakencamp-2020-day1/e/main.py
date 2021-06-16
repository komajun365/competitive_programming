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

x,y = map(int,input().split())

if x==y==0:
    print('1 1')
    exit()
if x == y:
    print(-1)
    exit()

rev = 0
if x > y:
    x,y = y,x
    rev = 1

if x == 0:
    a = y*2
    b = y
else:
    a = x+y
    b = y
if rev ==1:
    a,b = b,a

print(a,b)