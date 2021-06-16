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

n,a,b,*h = map(int,read().split())

def calc(x):
    cnt = 0
    xb = x*b
    for hi in h:
        if hi <= xb:
            continue
        hi -= xb
        cnt += -( -hi//(a-b) )
    return cnt <= x

ok = 10**15
ng = 0
while ok-ng > 1:
    mid = (ok+ng)//2
    if calc(mid):
        ok = mid
    else:
        ng = mid
print(ok)