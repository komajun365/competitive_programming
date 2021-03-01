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

import sys
read = sys.stdin.read

n,*data = read().split()
n = int(n)
s = data[:n]
uv = []
for i in range(n):
    uv.append([data[n+i*5], 0 if data[n+i*5+3] == 'good' else 1])

d = dict()
for i,si in enumerate(s):
    d[si] = i

ans = []
res = []
ans_l = 0
for i in range(1 << n):
    for j in range(n):
        u,v = uv[j]
        u = d[u]
        if ((i >> u) & 1) != (((i >> j) & 1) ^ v):
            # print(i,j,u,v)
            break
    else:
        res = []
        for j in range(n):
            if (i>>j) & 1 == 0:
                res.append(s[j])
        res.sort()
        if ans_l < len(res):
            ans = res[::]
            ans_l = len(res)
        elif ans_l == len(res) and ans > res:
            ans = res[::]
    # print(i,ans,res)

if ans_l == 0:
    print('No answers')
else:
    print('\n'.join(ans))

# print(s)
# print(uv)

# print('KONAN' > 'TONNELAT')