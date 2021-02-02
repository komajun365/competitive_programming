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

h,w = map(int,input().split())
n = int(input())
a = list(map(int,input().split()))

ans = []
for i,ai in enumerate(a,1):
    ans += [i]*ai

for i in range(h):
    tmp = ans[i*w:(i+1)*w]
    if(i%2==0):
        print(' '.join(map(str,tmp)))
    else:
        print(' '.join(map(str,tmp[::-1])))
