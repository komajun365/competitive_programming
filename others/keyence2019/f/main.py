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

h,w,k = map(int,input().split())
mod = 10**9+7

if k==1:
    ans = 2 * (h+w) % mod
    print(ans)
    exit()

h_k2 = 1
for i in range(k-2):
    h_k2 *= h+w-2-i
    h_k2 %= mod

com_k2 = 0
for i in range(1,k):
    com_k2 += i * (k-i)
    com_k2 %= mod

h_k1 = h_k2 * (h+w-1) % mod
com_k1 = k * (k+1) //2 % mod
h_k0 = h_k1 * (h+w) % mod

ans = (h_k2 * com_k2 % mod) * (h * w % mod) * 2 % mod
ans += (h_k1 * com_k1 % mod) * (h+w) % mod
ans += h_k0 * k % mod
ans %= mod

print(ans)
# print(h_k2,com_k2,h_k1,com_k1,h_k0)