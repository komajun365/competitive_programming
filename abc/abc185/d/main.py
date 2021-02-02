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

# from math import gcd

n,m = map(int,input().split())
if(m==0):
    print(1)
    exit()
a = list(map(int,input().split())) + [0,n+1]
a.sort()
x = []
for i in range(m+1):
    if a[i+1]-a[i] != 1:
        x.append(a[i+1]-a[i]-1)

x.sort()
ans = 0
for xi in x:
    ans += -1*(-xi//x[0])
print(ans)
# print(x)