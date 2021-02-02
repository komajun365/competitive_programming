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

n,m,*xy = map(int,read().split())
# if(n==16):
#     exit()

order = [[0] * n for _ in range(n)]
it = iter(xy)
for x,y in zip(it,it):
    x -= 1
    y -= 1
    order[x][y] = 1
    order[y][x] = -1

n2 = 2**n
dp = [[0] * n for _ in range(n2)]
for i in range(n):
    for j in range(n):
        if(order[i][j] == -1):
            break
    else:
        dp[1<<i][i] = 1

for bi in range(1,n2):
    for j in range(n):
        if(bi >> j)&1:
            bef = []
            cnt = 0
            for i in range(n):
                if(i==j) or (((bi>>i)&1)==0):
                    continue
                if order[i][j] == -1:
                    cnt += 1
                    continue
                bef.append(i)
            if(cnt > 0):
                continue
            for i in bef:
                # print(i,j,bi)
                dp[bi][j] += dp[bi ^ (1<<j)][i]

ans = sum(dp[-1])
print(ans)

# for i in range(n2):
#     print(i,dp[i])

'''
n+n+1個の


'''