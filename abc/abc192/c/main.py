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

n,k = map(int,input().split())

x = n
for i in range(k):
    g1 = list(str(x))
    g1.sort()
    g2 = g1[::-1]
    x = 0
    for j1,j2 in zip(g1,g2):
        x = x*10 + int(j2) - int(j1)

print(x) 