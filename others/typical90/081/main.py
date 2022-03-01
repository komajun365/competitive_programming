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

n,k,*ab = map(int,read().split())
m = 5001

cnt = [[0] * m for _ in range(m)]
it = iter(ab)
for a,b in zip(it,it):
    cnt[a][b] += 1

for i in range(m):
    for j in range(1,m):
        cnt[i][j] += cnt[i][j-1]

for i in range(1,m):
    for j in range(m):
        cnt[i][j] += cnt[i-1][j]

ans = 0
for i in range(k+1,m):
    for j in range(k+1,m):
        ans = max(ans, cnt[i][j] - cnt[i-k-1][j] - cnt[i][j-k-1] + cnt[i-k-1][j-k-1])
print(ans)
