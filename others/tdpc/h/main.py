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

N,W,C,*data = map(int,read().split())

wvc = [[] for _ in range(50)]
it = iter(data)
for w,v,c in zip(it,it,it):
    c -= 1
    wvc[c].append([w,v])

dp = [[0] * (W+1) for _ in range(C+1)]
for ci in range(50):
    for i in range(min(ci+1, C),0,-1):
        dp_i = dp[i-1][::]
        for w,v in wvc[ci]:
            for j in range(W,w-1,-1):
                dp_i[j] = max(dp_i[j-w] + v, dp_i[j])
        for j in range(W+1):
            dp[i][j] = max(dp[i][j], dp_i[j])

ans = 0
for i in dp:
    ans = max(ans, max(i))
print(ans)


