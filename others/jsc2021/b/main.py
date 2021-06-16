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

n,m = map(int,input().split())
a = list(map(int,input().split()))
b = list(map(int,input().split()))

set_a = set(a)
set_b = set(b)
ans = []
for ai in a:
    if not ai in set_b:
        ans.append(ai)
for bi in b:
    if not bi in set_a:
        ans.append(bi)
ans.sort()

print(' '.join(map(str,ans)))