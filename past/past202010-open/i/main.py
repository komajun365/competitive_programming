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

n = int(input())
a = list(map(int,input().split()))
tot = sum(a)
a += a
cs = [0] * (2*n+1)
for i,ai in enumerate(a):
    cs[i+1] = cs[i] + ai

lim = tot//2
max_sum = 0
l = 0
for i in range(2*n+1):
    while(cs[i] - cs[l] > lim):
        l += 1
    max_sum = max(max_sum, cs[i] - cs[l])

ans = tot - max_sum*2
print(ans)
