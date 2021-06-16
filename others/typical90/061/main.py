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

q,*tx = map(int,read().split())

up = []
down = []
ans = []
it = iter(tx)
for t,x in zip(it,it):
    if t == 1:
        up.append(x)
    elif t == 2:
        down.append(x)
    else:
        if len(up) >= x:
            ans.append(up[-x])
        else:
            x -= len(up)
            ans.append(down[x-1])
print('\n'.join(map(str,ans)))
