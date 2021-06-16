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

ans = 2**30
for i in range(2**(n-1)):
    res = 0
    tmp = 0
    for j in range(n):
        tmp |= a[j]
        if (i >> j) & 1==0:
            res ^= tmp
            tmp = 0
    ans = min(ans, res)

print(ans)

