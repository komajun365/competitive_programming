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

n = int(input())
a = list(map(int,input().split()))
mod = 10**9 + 7

ap = a[0]
am = 0
p = 1
m = 0
for i in range(1,n):
    ai = a[i]
    p,m = p+m,p
    p %= mod
    ap,am = (ap + am + ai * p) % mod, (ap - ai*m) % mod
    # print(p,m,ap,am)

ans = (ap+am) % mod
print(ans)