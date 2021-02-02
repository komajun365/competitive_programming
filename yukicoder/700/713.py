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

ans = 0
sieve = [True] * (n+1)
sieve[0] = False
sieve[1] = False
for i in range(2,n+1):
    if(sieve[i]):
        ans += i
        for j in range(i*2,n+1,i):
            sieve[j] = False

print(ans)
