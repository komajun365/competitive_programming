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

r,c,d,*a = map(int,read().split())

ans = 0
for i in range(r):
    for j in range(c):
        if (i+j-d) % 2 == 1:
            continue
        if i+j > d:
            continue
        ans = max(ans,a[i*c+j])
print(ans)