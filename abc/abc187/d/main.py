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

n,*ab = map(int,read().split())
aoki = 0
tak = []
it = iter(ab)
for a,b in zip(it,it):
    aoki += a
    tak.append(a*2+b)

tak.sort(reverse=True)
tot = 0
for i,ti in enumerate(tak,1):
    tot += ti
    if(tot > aoki):
        print(i)
        exit()

# print(tak)