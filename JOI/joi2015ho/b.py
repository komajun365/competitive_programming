# a,b = map(int,input().split())
# a = list(map(int,input().split()))
# a = [list(map(int,input().split())) for _ in range(n)]

# import sys
# read = sys.stdin.buffer.read
# readline = sys.stdin.buffer.readline
# readlines = sys.stdin.buffer.readlines

# 検討?分　実装分 バグとり分

import sys
import os
f = open('../../input.txt', 'r')
sys.stdin = f

import sys
read = sys.stdin.buffer.read
n,*a = map(int,read().split())

if n == 2:
    print(max(a))
    exit()

a += a

dp = [[-1]* n for _ in range(n)]
for i in range(n):
    dp[i][i] = 0

for d in range(n//2):
    d *= 2
    for l in range(n):
        r = l-d
        if dp[l][r] == -1:
            continue
        if a[l+1] > a[r-1]:
            dp[(l+2)%n][r] = max(dp[(l+2)%n][r], dp[l][r] + a[l])
        else:
            dp[(l+1)%n][r-1] = max(dp[(l+1)%n][r-1], dp[l][r] + a[l])
        if a[l] > a[r-2]:
            dp[(l+1)%n][r-1] = max(dp[(l+1)%n][r-1], dp[l][r] + a[r-1])
        else:
            dp[l][r-2] = max(dp[l][r-2], dp[l][r] + a[r-1])

ans = 0
d = (n//2)*2
for l in range(n):
    r = l+(n-d)
    if dp[l][r%n] == -1:
        continue
    if d == n:
        ans = max(ans, dp[l][l])
    else:
        ans = max(ans, dp[l][r%n] + a[l])
print(ans)






# inf = 10**15

# for d in range(1,n):
#     for l in range(n):
#         r = (l+d) % n
#         if (n-d+1) % 2 == 0:
#             dp[l][r] = max(a[r-1] - dp[l][r-1], a[l] - dp[(l+1)%n][r])
#         else:
#             dp[l][r] = max(a[r-1] - dp[l][r-1], a[l] - dp[(l+1)%n][r])

# ans = 0
# for l in range(n):
#     ans = max(ans, a[l-1] - dp[l][l-1])

# ans = (sum(a) + ans)//2
# print(ans)

# for i in range(n):
#     print(a[i-1], dp[i][i-1])
    

'''
dp[l][r] := l~r-1まで残っているとき

dp[l][l+1] := a[l]
dp[l][r] = max(a[r-1] - dp[l][r-1], a[l] - dp[l+1][r])

'''

