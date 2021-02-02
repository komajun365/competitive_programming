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

h1,w1 = map(int,input().split())
h2,w2 = map(int,input().split())
if(h1 == h2) or (h1 == w2) or (w1 == h2) or (w1 == w2):
    print('YES')
else:
    print('NO')