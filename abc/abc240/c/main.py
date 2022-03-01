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

import sys
read = sys.stdin.buffer.read

n,x,*ab = map(int,read().split())

dp = 1
it = iter(ab)
for ai,bi in zip(it,it):
    dp = (dp<<ai) | (dp<<bi)
if (dp >> x) & 1:
    print('Yes')
else:
    print('No')