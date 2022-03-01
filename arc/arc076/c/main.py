# oj t -c "python main.py" -d "./tests/" 

# a,b = map(int,input().split())
# a = list(map(int,input().split()))
# a = [list(map(int,input().split())) for _ in range(n)]

# import sys
# read = sys.stdin.buffer.read
# readline = sys.stdin.buffer.readline
# readlines = sys.stdin.buffer.readlines

# 検討?分　実装分 バグとり分

# import sys
# import os
# f = open('../../../input.txt', 'r')
# sys.stdin = f

n,m = map(int,input().split())
mod = 10**9 + 7

if n > m:
    n,m = m,n

if m-n >= 2:
    print(0)
    exit()

ans = 1
for i in range(1,n+1):
    ans *= i
    ans %= mod
for i in range(1,m+1):
    ans *= i
    ans %= mod

if n == m:
    ans *= 2
    ans %= mod

print(ans)