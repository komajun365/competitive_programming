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
f = open('p018_triangle.txt', 'r')
sys.stdin = f

i = 1
fi = 1
fj = 1

lim = 10**999
while(fi < lim):
    fi,fj = fj,fi+fj
    i += 1

print(i)


'''
普通に計算できそう

'''
