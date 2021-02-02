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

n,m,*ab = map(int,read().split())
if(m==0):
    print(n)
    exit()

link = [[0] * n for _ in range(n)]
it = iter(ab)
for a,b in zip(it,it):
    a -= 1
    b -= 1
    link[a][b] = 1
    link[b][a] = 1

n2 = 2**n
kr = [0] * n2
kr[0] = 1
kr[1] = 1
for i in range(1,n):
    for j in range(2**i):
        flag = kr[j]

        for bi in range(i):
            if(j >> bi)&1:
                if(link[i][bi] == 0) :
                    flag = 0
                    break
        kr[2**i + j] = flag

inf = 20
dp = [inf] * n2
for i in range(n2):
    if(kr[i] == 1):
        dp[i] = 1
    
    y = (i-1) & i
    while(y > 0):
        dp[i] = min(dp[i], dp[y] + dp[i-y])
        y = (y-1) & i

print(dp[-1])



# from functools import lru_cache
# @lru_cache(maxsize=10**9)
# def calc(x):
#     if(kr[x] == 1):
#         return 1
    
#     res = 0
#     for i in range(18):
#         if( x >> i)&1:
#             res += 1
#     y = (x-1) & x
#     while(y > 0):
#         if(kr[y] == 1):
#             res = min(res, 1 + calc(x-y))
#         y = (y-1) & x
#     return res

# print(calc(2**n-1))





# inf = 20
# n2 = 2**n
# dp = [inf] * n2
# dp[0] = 0
# for i in range(n):
#     mask = 2**i -1
#     dp[2**i] = dp[2**i-1] + 1
#     for j in range(1,2**i):
#         k = mask - j
#         flag = True
#         for bi in range(i):
#             if(j >> bi)&1:
#                 if(link[i][bi] == 0):
#                     flag = False
#                     break
#         if flag:
#             dp[ 2**i + j] = dp[j] + dp[k]
#         else:
#             dp[ 2**i + j] = dp[j] + dp[k] + 1

# ans = inf
# for i in range(2**(n-1), 2**n):
#     ans = min(ans,dp[i])

# print(ans)

# print(dp)

# # kreek = [0] * n2
# # kreek[0] = 1
# # for i in range(n2):




# # dp = [[inf] * n2 for _ in range(n+1)]
# # dp[0][0] = 1
# # for i in range(n):
# #     for j in range(2**i):
# #         if(j == 0):



