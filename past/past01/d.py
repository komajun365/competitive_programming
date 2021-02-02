# a,b = map(int,input().split())
# a = list(map(int,input().split()))
# a = [list(map(int,input().split())) for _ in range(n)]

# 検討?分　実装分 バグとり分

import sys
import os
f = open('../../input.txt', 'r')
sys.stdin = f

import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

n = int(readline())
a = list(map(int, read().split()))

cnt = [0]*(n)
for i in a:
    cnt[i-1] += 1

ans0 = -1
ans2 = -1
for ind,val in enumerate(cnt,1):
    if(val==0):
        ans0 = ind
    if(val==2):
        ans2 = ind

if(ans0==-1):
    print('Correct')
else:
    print('{} {}'.format(ans2,ans0))
