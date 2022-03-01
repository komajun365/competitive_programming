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

cnt = [0] * (10**5+1)
ans = 0
l = 0
for r in range(n):
    ar = a[r]
    cnt[ar] += 1
    while cnt[ar] > 1:
        cnt[a[l]] -= 1
        l += 1
    ans = max(ans, r-l+1)
print(ans)

