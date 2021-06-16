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


h,w = map(int,input().split())
mod = 998244353
h2 = 2**h

def mat_mul(x,y):
    n = len(x)
    res = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                res[i][j] += x[i][k] * y[k][j]
                res[i][j] %= mod
    return res

pattern = [0] * h2
for i in range(h2):
    open = [0] * h
    for j in range(h):
        if (i >> j) & 1 == 0:
            open[j] = 1
    dp = [0] * (h+1)
    dp[0] = 1
    for j in range(1,h+1):
        dp[j] = dp[j-1]
        if j >= 2:
            if open[j-2] == open[j-1] == 1:
                dp[j] += dp[j-2]
    pattern[i] = dp[-1]

# print(pattern)

mat = [[0]*h2 for _ in range(h2)]
for i in range(h2):
    for j in range(h2):
        if i & j > 0:
            continue
        x = i | j
        mat[i][j] = pattern[x]

mat_ex = []
mat_ex.append(mat)
for _ in range(40):
    mat_ex.append(mat_mul(mat_ex[-1],mat_ex[-1]))

mat_ans = [[0]*h2 for _ in range(h2)]
for i in range(h2):
    mat_ans[i][i] = 1

for i in range(41):
    if (w >> i) & 1:
        mat_ans = mat_mul(mat_ex[i], mat_ans)

print(mat_ans[0][0])

# print(mat_ex[0])
# print(mat_ex[1])