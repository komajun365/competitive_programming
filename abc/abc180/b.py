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
x = list(map(int,input().split()))

man = 0
euq = 0
che = 0
for xi in x:
    man += abs(xi)
    euq += xi**2
    che = max(che,abs(xi))

euq = euq ** 0.5
print(man)
print(euq)
print(che)