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
a = list(map(int,input().split()))

bl =k.bit_length() + 1
mask = (1 << 20) - 1

# dbl = []
# dbl.append([0] * n)
dbl1 = [[0] * n for _ in range(bl)]
dbl2 = [[0] * n for _ in range(bl)]
for i in range(n):
    dbl1[0][i] = a[i]
    dbl2[0][i] = (i + a[i]) % n

for j in range(1,bl):
    for i in range(n):
        tot1 = dbl1[j-1][i]
        n1 = dbl2[j-1][i]
        tot2 = dbl1[j-1][n1]
        n2 = dbl2[j-1][n1]
        dbl1[j][i] = tot1 + tot2
        dbl2[j][i] = n2

now = 0
ans = 0
for j in range(bl):
    if (k >> j) & 1:
        ans += dbl1[j][now]
        now = dbl2[j][now]

print(ans)


