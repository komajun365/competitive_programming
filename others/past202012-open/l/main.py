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
s = input()
t = input()

dp = [[0] * (n+1) for _ in range(n)]
for i in range(n):
    dp[i][i] = 1

for d in range(3,n+1,3):
    for l in range(n-d+1):
        r = l+d
        x2 = r-1
        if s[x2] != t[2]:
            continue
        for x0 in range(l,x2-1):
            if s[x0] != t[0]:
                continue
            for x1 in range(x0+1,x2):
                if s[x1] != t[1]:
                    continue
                if dp[l][x0] == 1 and dp[x0+1][x1] == 1 and dp[x1+1][x2] == 1:
                    dp[l][r] = 1

dp2 = [0] * (n+1)
for i in range(1,n+1):
    dp2[i] = dp2[i-1]
    for j in range(i):
        if dp[j][i] == 1:
            # print(i,j)
            # print(dp2[i], dp2[j] + (i-j)//3)
            dp2[i] = max(dp2[i], dp2[j] + (i-j)//3)
print(dp2[-1])

# print(dp2)
# ans = 0
# for i in range(n):
#     for j in range(n+1):
#         if dp[i][j] == 1:
#             ans = max(ans, j-i)
# ans //= 3
# print(ans)

# for i in dp:
#     print(i)

