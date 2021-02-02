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
a = [-1000000] + list(map(int,input().split()))

dp = [0] * (n+1)
for i in range(2,n+1):
    dp[i] = min(dp[i-2] + abs(a[i]-a[i-2]),
                dp[i-1] + abs(a[i]-a[i-1]))
print(dp[-1])