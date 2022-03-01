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

cnt = [0] * (10**5+10)
for ai in a:
    cnt[ai] += 1

ans = 0
for i in range(10**5+1):
    tmp = cnt[i] + cnt[i-1] + cnt[i+1]
    ans = max(ans,tmp)

print(ans)