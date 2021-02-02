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
ng = set()
for _ in range(3):
    ng.add(int(input()))

if( n in ng) :
    print(('NO'))
    exit()

dp = [-1] * (n+10)
dp[n] = 100
for i in range(n-1,-1,-1):
    if(i in ng):
        continue
    for j in range(1,4):
        if(dp[i+j] > 0):
            dp[i] = max(dp[i], dp[i+j]-1)

if(dp[0] >= 0):
    print('YES')
else:
    print('NO')