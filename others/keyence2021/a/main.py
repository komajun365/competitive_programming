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
b = list(map(int,input().split()))

max_a = 1
max_ab = 1
ans = []
for ai,bi in zip(a,b):
    max_a = max(max_a,ai)
    max_ab = max(max_ab, max_a * bi)
    ans.append(max_ab)


print('\n'.join(map(str,ans)))