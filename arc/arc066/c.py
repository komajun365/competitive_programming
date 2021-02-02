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

n = int(input())
a = list(map(int,input().split()))
mod = 10**9 + 7

a.sort()
b = [ abs((n-1-i) - i)  for i in range(n)]
b.sort()

for ai,bi in zip(a,b):
    if(ai!=bi):
        print(0)
        exit()

ans = pow(2, n//2 ,mod)
print(ans)
