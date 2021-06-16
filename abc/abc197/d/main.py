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

import math

n = int(input())
x0,y0= map(int,input().split())
x2,y2 = map(int,input().split())

x = (x0+x2)/2
y = (y0+y2)/2
bx = (x0-x2)/2
by = (y0-y2)/2

rad = math.radians( 360/n )
x += math.cos(rad) * bx - math.sin(rad) * by
y += math.sin(rad) * bx + math.cos(rad) * by

print(x, y)
# print(bx,by)