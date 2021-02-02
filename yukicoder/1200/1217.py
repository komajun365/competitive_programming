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

base = 'abcdefghijklmnopqrstuvwxyz'
s = input()
for bi,si in zip(base,s):
    if(bi != si):
        print(bi+'to'+si)
        exit()
