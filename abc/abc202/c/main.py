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
b = list(map(int,input().split()))
c = list(map(int,input().split()))

cnt_b = [0] * n
for ci in c:
    ci -= 1
    cnt_b[ci] += 1

nums = [0] * (n+1)
for i in range(n):
    bi = b[i]
    nums[bi] += cnt_b[i]

ans = 0
for ai in a:
    ans += nums[ai]
print(ans)

