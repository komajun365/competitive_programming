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
read = sys.stdin.read

n,*data = read().split()

tot = 0
it = iter(data)
for s,p in zip(it,it):
    p = int(p)
    tot += p

ans = 'atcoder'
it = iter(data)
for s,p in zip(it,it):
    p = int(p)
    if p*2 > tot:
        ans = s
print(ans)