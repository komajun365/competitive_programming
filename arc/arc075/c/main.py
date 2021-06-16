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

n,*s = map(int,read().split())
n2 = n*100

dp = [0] * (n2+1)
dp[0] = 1

for si in s:
    for j in range(n2-si,-1,-1):
        if dp[j] == 1:
            dp[j+si] = 1

ans = 0
for j in range(n2+1):
    if j%10 != 0 and dp[j] == 1:
        ans = j

print(ans)
