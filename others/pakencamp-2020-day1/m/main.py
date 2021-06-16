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
a = list(map(int,input().split()))

dp = [0] * (2**20)

for ai in a:
    dp[ai] = ai

ans = 0
for i in range(1,2**20):
    if dp[i] == i:
        ans += 1
    
    for j in range(20):
        if (i>>j) & 1 == 0:
            dp[i | (1<<j)] |= dp[i]

print(ans)

'''
10001
00100
00011
00001

1
3
4
5
7
17
19
21
23



'''