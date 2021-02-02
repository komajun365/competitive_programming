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

n,k = map(int,input().split())
if(k==0):
    print(n*n)
    exit()
ans = 0
for i in range(k+1,n+1):
    ans += (n//i) * (i-k)
    ans += max(0, n%i-k+1)
print(ans)
