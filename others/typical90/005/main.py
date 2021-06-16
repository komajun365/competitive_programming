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

n,b,k = map(int,input().split())
c = list(map(int,input().split()))
mod = 10**9 + 7

dbl = [[0] * b for _ in range(60)]

for ci in c:
    dbl[0][ci % b] += 1


ex = 10 % b
ex10 = [ex]
for i in range(1,60):
    for j in range(b):
        for l in range(b):
            go = (j * ex + l) % b
            dbl[i][go] += dbl[i-1][j] * dbl[i-1][l]
            dbl[i][go] %= mod
    
    ex = ex**2 % b
    ex10.append(ex)
    # print(dbl[i-1])

ans = [0] * b
ans[0] = 1
for i in range(60):
    if (n >> i) & 1:
        ans2 = [0] * b
        for j in range(b):
            for l in range(b):
                go = (j * ex10[i] + l) % b
                ans2[go] += ans[j] * dbl[i][l]
                ans2[go] %= mod
        ans,ans2 = ans2,ans
    # print(ans)

print(ans[0])

# print(ex10)

