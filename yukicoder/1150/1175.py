# a,b = map(int,input().split())
# a = list(map(int,input().split()))
# a = [list(map(int,input().split())) for _ in range(n)]

# import sys
# read = sys.stdin.buffer.read
# readline = sys.stdin.buffer.readline
# readlines = sys.stdin.buffer.readlines

# 検討?分　実装分 バグとり分

import sys
import os
f = open('../../input.txt', 'r')
sys.stdin = f

a,b,c,d,e,f = map(int,input().split())

x = c*e-b*f
y = -c*d+a*f
x /= a*e-b*d
y /= a*e-b*d
print(' '.join(map(str,[x,y])))
