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

n,*c = map(int,read().split())

a = [i for i in c[::n]]
b = c[:n]
min_a = min(a)
min_b = min(b)
for i in range(n):
    a[i] -= min_a
    b[i] -= min_b

dif = c[0] - a[0] - b[0]
for i in range(n):
    a[i] += dif

for i in range(n):
    for j in range(n):
        if c[i*n+j] != a[i] + b[j]:
            print('No')
            exit()

print('Yes')
print(*a, sep=' ')
print(*b, sep=' ')
