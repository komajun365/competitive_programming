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

n,*uv = map(int,read().split())

vs = 0
for i in range(n):
    vs += (i+1) * (n-i)

edges = 0
it = iter(uv)
for u,v in zip(it,it):
    if(u > v):
        u,v = v,u
    edges += u * (n-v+1)

print(vs-edges)

'''
連結成分の数　＝　頂点-辺の数

'''