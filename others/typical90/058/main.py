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

n,k = map(int, input().split())

m = 10**5
dbl = [[0] for _ in range(m)]
for i in range(m):
    x = i
    tmp = i
    while x > 0:
        tmp += x%10
        x //= 10
    tmp %= m
    dbl[i][0] = tmp

for j in range(1,60):
    for i in range(m):
        dbl[i].append(dbl[dbl[i][j-1]][j-1])

ans = n
for j in range(60):
    if (k >> j) & 1:
        ans = dbl[ans][j]
print(ans)

# print(dbl[0:10])

# for i in range(10):
#     for j in range(10):
#         print(dbl[i][:j])

