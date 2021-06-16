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

n,k = map(int,input().split())

cnt = [0] * (n+1)
ans = 0
for i in range(2,n+1):
    if cnt[i] == 0:
        for j in range(i,n+1,i):
            cnt[j] += 1
    if cnt[i] >= k:
        ans += 1
print(ans)

