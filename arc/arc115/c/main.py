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

ans = [2] * (n+1)
ans[1] = 1
for i in range(2,n+1):
    for j in range(i*2,n+1,i):
        ans[j] = max(ans[j], ans[i]+1)

print(*ans[1:], sep=' ')
