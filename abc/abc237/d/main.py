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

from collections import deque

n = int(input())
s = input()

d = deque()
d.append(n)

for i in range(n-1,-1,-1):
    if s[i] == 'R':
        d.appendleft(i)
    else:
        d.append(i)

print(*d, sep=' ')