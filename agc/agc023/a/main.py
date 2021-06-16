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

from collections import defaultdict

n = int(input())
a = list(map(int,input().split()))

right = defaultdict(int)
right[0] += 1
cs = [0] * (n+1)
for i in range(n-1,-1,-1):
    cs[i] = cs[i+1] + a[i]
    right[cs[i]] += 1

tot = cs[0]
left = 0
ans = 0
for i in range(n):
    right[cs[i]] -= 1
    ans += right[tot-left]
    left += a[i]

print(ans)
