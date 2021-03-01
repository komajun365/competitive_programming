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

n,*apx = map(int,read().split())

inf = 10**10
ans = inf
it = iter(apx)
for a,p,x in zip(it,it,it):
    if x > a:
        ans = min(ans, p)

if ans == inf:
    print(-1)
else:
    print(ans)

