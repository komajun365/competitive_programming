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
import itertools

n,k,*t = map(int,read().split())

ans = 0
for ps in itertools.permutations(range(n)):
    i = ps[-1]
    tmp = 0
    for j in ps:
        tmp += t[i*n+j]
        i = j
    if(tmp == k):
        ans += 1

print(ans//n)

