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

n,m,k = map(int,input().split())
mod = 998244353

if n == m == 1:
    print(k % mod)
    exit()

if n == 1 or m == 1:
    if n > m:
        n,m = m,n
    ans = pow(k,m,mod)
    print(ans)
    exit()

# cs = [0] * (2*10**5 + 1)
# for i in range(1,2*10**5 + 1):
#     cs[i] = cs[i-1] + pow(i,m,mod)
#     cs[i] %= mod

ans = 0
for i in range(1,k+1):
    ans += (pow(i,n,mod) - pow(i-1,n,mod)) * pow(k-i+1,m,mod)
    ans %= mod

print(ans)
