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

n = int(input())
s = list(map(int,input().split()))
t = list(map(int,input().split()))
u = list(map(int,input().split()))



'''
3
2 1 2
3 3 1
3 1 0

A21 + A13*2 ≠ 3
A22 + A23*2 ≠ 3
A23 + A33*2 ≠ 3

A11 + A13*2 ≠ 1
A12 + A23*2 ≠ 1
A13 + A33*2 ≠ 1

A21 + A11*2 ≠ 0
A22 + A21*2 ≠ 0
A23 + A31*2 ≠ 0

000   0
101 * 1
000   0

0   000
2 * 101
0   000


'''
