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
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

n,m,a,b = map(int,readline().split())
if(m==0):
    print('complete')
    exit()

c = [0] + list(map(int,read().split()))
for i,ci in enumerate(c):
    n -= ci
    if(n < 0):
        print(i)
        exit()
    if(n <= a):
        n += b
print('complete')

