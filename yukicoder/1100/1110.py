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

n,d = map(int,readline().split())
a = [ (int(ai),i) for i,ai in enumerate(read().split())]
a.sort()

ans = [0] * n
left = 0
for right in range(n):
    while(a[left][0] + d <= a[right][0]):
        left += 1
    ans[ a[right][1] ] = left

print('\n'.join(map(str,ans)))
