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

n = int(readline())
ab = list(map(int,read().split()))
a = ab[::2]
b = ab[1::2]
a.sort()
b.sort()

if(n%2==1):
    n_min = a[n//2]
    n_max = b[n//2]
    ans = n_max-n_min+1
else:
    n_min = a[n//2 -1] + a[n//2]
    n_max = b[n//2 -1] + b[n//2]
    ans = n_max-n_min+1

print(ans)
