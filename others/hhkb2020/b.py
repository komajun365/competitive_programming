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

import sys
read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines

h,w,*s = read().split()
h = int(h)
w = int(w)
ans = 0
for i in range(h):
    for j in range(w-1):
        if(s[i][j]=='.')&(s[i][j+1]=='.'):
            ans += 1

for i in range(h-1):
    for j in range(w):
        if(s[i][j]=='.')&(s[i+1][j]=='.'):
            ans += 1

print(ans)
