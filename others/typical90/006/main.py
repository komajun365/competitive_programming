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

n,k = map(int,input().split())
s = input()

dq = deque()

def append_dq(x):
    while dq:
        if dq[-1] <= x:
            break
        dq.pop()
    dq.append(x)

ans = ''

for i in range(n-k):
    append_dq(s[i])

for i in range(n-k,n):
    append_dq(s[i])
    ans += dq.popleft()

print(ans)
