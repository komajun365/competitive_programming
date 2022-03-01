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
w = list(map(int,input().split()))
mod = 998244353

# w.sort()

# dp = [[0] * 101 for _ in range(n+1)]
# dp[0][0] = 1

# for i in range()


import itertools
def solve_simple(n,w):
    res = 0
    for p in itertools.permutations(range(n)):
        tmp = 0
        for i in p:
            tmp = abs(tmp - w[i])
        if tmp == 0:
            res += 1
    return res

print(solve_simple(n,w))