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

n,k = map(int,input().split())
a = list(map(int,input().split()))
b = list(map(int,input().split()))

dif = 0
for i in range(n):
    dif += abs(a[i]-b[i])
if dif <= k and (k-dif)%2==0:
    print('Yes')
else:
    print('No')