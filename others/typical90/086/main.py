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

n,q,*xyzw = map(int,read().split())
mod = 10**9 + 7

ans = 1
for i in range(60):
    cnt = 0
    for bi in range(1<<n):
        bi *= 2
        it = iter(xyzw)
        for x,y,z,w in zip(it,it,it,it):
            x = (bi >> x)&1
            y = (bi >> y)&1
            z = (bi >> z)&1
            w = (w >> i)&1
            if x | y | z != w:
                break
        else:
            cnt += 1
    ans *= cnt
    ans %= mod
print(ans)