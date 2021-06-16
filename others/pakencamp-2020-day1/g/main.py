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

n,m,*data = map(int,read().split())

it = iter(data)
lrx = [[l-1,r-1,x] for l,r,x in zip(it,it,it)]

ans = -1
for bit in range(1<<n):
    cs = [0] * (n+1)
    for i in range(n):
        cs[i] = cs[i-1] + 1 * ((bit>>i)&1)
    
    for l,r,x in lrx:
        if cs[r] - cs[l-1] != x:
            break
    else:
        ans = max(ans, cs[n-1])

print(ans)

