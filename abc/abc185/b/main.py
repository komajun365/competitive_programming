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
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

n,m,t, *ab = map(int,read().split())
it = iter(ab)
ab += [t,t+1]
x = n
bef = 0
for a,b in zip(it,it):
    x -= a - bef
    if(x <= 0):
        print('No')
        exit()
    x = min(n, x+b-a)
    bef = b

print('Yes')