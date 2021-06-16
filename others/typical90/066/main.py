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

n,*lr = map(int,read().split())

ans = 0
for i in range(n-1):
    li,ri = lr[i*2:i*2+2]
    ri += 1
    for j in range(i+1,n):
        lj,rj = lr[j*2:j*2+2]
        rj += 1
        tmp = 0
        for x in range(li,ri):
            tmp += max(0, min(x,rj) - lj)
        ans += tmp / ((ri-li)*(rj-lj))

print(ans)

