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

# 解説AC

n = int(input())
a = list(map(int,input().split()))
t = int(input())
mod = 10**9 + 7

if t <= n:
    print(a[t])
    exit()

mul_p = [1] * (n+1)
mul_m = [1] * (n+1)
for i in range(1,n+1):
    mul_p[i] = mul_p[i-1] * i % mod
    mul_m[i] = mul_m[i-1] * (-i) % mod

c = [0] * (n+1)
for i in range(n+1):
    qii = 1
    qii *= mul_p[i]
    qii %= mod
    qii *= mul_m[n-i]
    qii %= mod
    c[i] = a[i] * pow(qii,mod-2,mod) % mod

qt_child = 1
for i in range(n+1):
    qt_child *= t-i
    qt_child %= mod

ans = 0
for i in range(n+1):
    ans += qt_child * c[i] * pow(t-i,mod-2,mod) % mod
    ans %= mod
print(ans)