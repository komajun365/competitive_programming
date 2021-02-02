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
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

c = int(readline())
nml = [sorted(list(map(int,i.split()))) for i in readlines()]
l = max( [max(i) for i in nml] )

ans = 100**3
for w in range(1,101):
    for h in range(w,101):
        for n,m,_ in nml:
            if(n > w)|(m > h):
                break
        else:
            ans = min(ans,w*h*l)
print(ans)
