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
m = int((2*n+2)**0.5) - 2

x = 0
for xi in range(m,m+10):
    tmp = (xi * (xi+1)) //2
    if( tmp > n+1):
        x = xi-1
        break

x = max(x,0)
# print(x)
print(n+1-x)


