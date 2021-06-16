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

cs = [0] * n
for i in range(n):
    if i % 2 == 0:
        cs[i] = cs[i-1] + a[i]
    else:
        cs[i] = cs[i-1] - a[i]
cs.append(0)

ans = 0
cnt = dict()
for i in cs:
    ans += cnt.get(i,0)
    cnt[i] = cnt.get(i,0) + 1
print(ans)
# print(cs)