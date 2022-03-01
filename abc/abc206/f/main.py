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

t,*data = map(int,read().split())


def calc(n,lr):
    it = iter(lr)
    lr2 = [[l-1,r-1] for l,r in zip(it,it)]
    
    dp = [[0] * 100 for _ in range(100)]
    for d in range(1,100):
        for i in range(100-d):
            j = i+d
            mex = 0
            done = set()
            for l,r in lr2:
                if i<=l and r<=j:
                    tmp = dp[i][l] ^ dp[r][j]
                    done.add(tmp)
                    while mex in done:
                        mex += 1
            dp[i][j] = mex
    if dp[0][-1] == 0:
        print('Bob')
    else:
        print('Alice')


idx = 0
for _ in range(t):
    n = data[idx]
    lr = data[idx+1:idx+1+n*2]
    idx += 1 + 2*n
    calc(n,lr)
