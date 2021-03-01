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
a1 = list(map(int,input().split()))
a2 = list(map(int,input().split()))

cs1 = [0]*n
for i in range(n):
    cs1[i] = cs1[i-1] + a1[i]

cs2 = [0]*(n+1)
for i in range(n-1,-1,-1):
    cs2[i] = cs2[i+1] + a2[i]

ans = 0
for i in range(n):
    ans = max(ans, cs1[i] + cs2[i])

print(ans)