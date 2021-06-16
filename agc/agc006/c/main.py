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
x = list(map(int,input().split()))
m,k = map(int,input().split())
a = list(map(int,input().split()))

l = 60
dbl = [[0] * l for _ in range(n-1)]

for i in range(n-1):
    dbl[i][0] = i

for ai in a:
    dbl[ai-2][0],dbl[ai-1][0] = dbl[ai-1][0],dbl[ai-2][0]

for i in range(1,l):
    for j in range(n-1):
        dbl[j][i] = dbl[ dbl[j][i-1] ][i-1]

last = list(range(n-1))
for i in range(l):
    for j in range(n-1):
        if (k >> i)&1:
            last[j] = dbl[ last[j] ][i]

dif = [0] * (n-1)
for i in range(n-1):
    dif[i] = x[i+1] - x[i]

ans = [0] * n
ans[0] = x[0]
for i in range(n-1):
    ans[i+1] = ans[i] + dif[ last[i] ]

print('\n'.join(map(str,ans)))