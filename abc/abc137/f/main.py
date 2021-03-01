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

p = int(input())
a = list(map(int,input().split()))

ans = [0] * p
ans[0] = a[0]
y = a[::]
for i in range(p-1,0,-1):
    tot = sum(y) % p
    ans[i] = (tot * (p-1)) % p
    for j in range(p):
        y[j] = (y[j] * j) % p

print(' '.join(map(str,ans)))