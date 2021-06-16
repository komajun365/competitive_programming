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

q,x,*a = map(int,read().split())
mod = 10**9 + 7

ans = x
ex2 = 1
for i in range(q):
    l = len(str(a[i]))
    ans = (ans * (1 + pow(10,l,mod)%mod) ) % mod
    ex2 *= 2
    ex2 %= mod
    ans += (a[i] * ex2) % mod
    ans %= mod
    # print(i,ans)

print(ans)


'''
4 10
12
21

1012,22
101221,1033,2221,43
104918


'''