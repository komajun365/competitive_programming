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

t,*case = map(int,read().split())

def calc(x):
    n = 100
    dp = [[x] for _ in range(n)]
    for i in range(17,0,-1):
        dp2 = [[x] for _ in range(n)]
        m = x
        base = 10**i
        for j in range(n):
            m = min(m, dp[j])
            l = base * j
            r = base * j * 3
            if x <= l:
                dp2[j] = x
            



            



for ci in case:
    print(calc(ci))
