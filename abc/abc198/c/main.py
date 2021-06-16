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

r,x,y = map(int,input().split())

tot = x**2 + y**2
if r**2 > tot:
    print(2)
    exit()
for i in range(1,10**6):
    if (r*i)**2 >= tot:
        print(i)
        exit()
    