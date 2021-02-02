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
s = [input() for _ in range(n)]

ans = [['']*n for _ in range(n)]
for i in range(n):
    for j in range(n):
        ans[j][n-1-i] = s[i][j]

for ai in ans:
    print(''.join(ai))