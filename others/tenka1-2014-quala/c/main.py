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

n,m = map(int,input().split())
p = []
for _ in range(n):
    p.append(input())

if n == 1:
    print(1)
    exit()

union = [[0] * n for _ in range(n)]
for i in range(n-1):
    for j in range(i+1,n):
        for idx in range(m):
            if p[i][idx] == '*':
                continue
            if p[j][idx] == '*':
                continue
            if p[i][idx] == p[j][idx]:
                continue
            break
        else:
            union[i][j] = 1
            union[j][i] = 1

def check_one(x):
    flags = []
    for i in range(n):
        if (x >> i) & 1:
            for j in flags:
                if union[i][j] == 0:
                    return False
            flags.append(i)
    return True

dp = [n] * (1<<n)
for i in range(1,1<<n):
    if check_one(i):
        dp[i] = 1
        continue

    x = (i-1) & i
    while x > 0:
        y = i ^ x
        dp[i] = min(dp[i],dp[x]+dp[y])
        x = (x-1) & i

print(dp[-1])
# print(dp)

# print(check_one(1))

    
            
