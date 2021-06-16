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

a = int(input())
b = int(input())
c = int(input())
mod = 10**9 + 7
d = (b+c) % mod

rc1 = b * c * pow((a*d-b*c), mod-2, mod) % mod
c1 = a * rc1 * pow(b,mod-2,mod) % mod
x = (rc1- c1) % mod
y = (c1-1) % mod

print(x,y)