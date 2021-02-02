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

s = input()
t = input()
for si,ti in zip(s,t):
    if(si==ti):
        continue
    elif(si=='@')&(ti in 'atcoder'):
        continue
    elif(ti=='@')&(si in 'atcoder'):
        continue
    else:
        print('You will lose')
        exit()

print('You can win')
