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
n = len(s)

for i in range(n-1):
    if(s[i]==s[i+1]):
        print('{} {}'.format(i+1,i+2))
        exit()

for i in range(n-2):
    if(s[i]==s[i+2]):
        print('{} {}'.format(i+1,i+3))
        exit()

print('{} {}'.format(-1,-1))
