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

d = dict()
for ai in a:
    d[ai] = d.get(ai, 0) + 1

for bi in b:
    if d.get(bi,0) == 0:
        print('No')
        exit()
    d[bi] -= 1

print('Yes')