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

a,v = map(int,input().split())
b,w = map(int,input().split())
t = int(input())

if(abs(a-b) <= (v-w)*t):
    print('YES')
else:
    print('NO')
