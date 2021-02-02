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

s=input()
n=len(s)
b_start = 0
w_start = 0
for i in range(n):
    if(i%2==0):
        b_start += (s[i]=='1')
        w_start += (s[i]=='0')
    else:
        b_start += (s[i]=='0')
        w_start += (s[i]=='1')

print(min(b_start,w_start))
