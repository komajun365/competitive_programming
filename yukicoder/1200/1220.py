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
import math

q = int(readline())
data = list(map(int,read().split()))

fr_log = [0] * (10**5+10)
for i in range(2,10**5+10):
    fr_log[i] = fr_log[i-1] + math.log(i)

ans = []
it = iter(data)
for n,m,k in zip(it,it,it):
    fn = math.log(m) + fr_log[n] - fr_log[n-k] - fr_log[k]
    sn = math.log(n-k+1) + k*math.log(m)
    if(fn < sn):
        ans.append('Flush')
    else:
        ans.append('Straight')

print('\n'.join(ans))
