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
a = list(map(int,input().split()))

dq = deque()
for i in range(n):
    if i % 2 == 0:
        dq.appendleft(a[i])
    else:
        dq.append(a[i])

ans = list(dq)
if n % 2 == 0:
    ans = ans[::-1]

print(' '.join(map(str,ans)))
