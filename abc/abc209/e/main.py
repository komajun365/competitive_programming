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

n,*s = read().split()
n = int(n)

tails = set()
for si in s:
    tails.add(si[:3])
    tails.add(si[-3:])

tails = list(tails)
encode = dict()
for i,ti in enumerate(tails):
    encode[ti] = i

m = len(tails)
links_rev = [set() for _ in range(m)]
deg_out = [0] * m
s2 = []
for si in s:
    h = encode[si[:3]]
    t = encode[si[-3:]]
    s2.append(t)
    links_rev[t].add(h)
    deg_out[h] += 1

result = [-1] * m # -1=draw,0=lose,1=win
stack = []
for i in range(m):
    if deg_out[i] == 0:
        stack.append(i)
        result[i] = 1

while stack:
    i = stack.pop()
    for j in links_rev[i]:
        if result[j] != -1:
            continue
        result[j] = 0
        deg_out[j] -= 1
        for k in links_rev[j]:
            if result[k] != -1:
                continue
            deg_out[k] -= 1
            if deg_out[k] == 0:
                stack.append(k)
                result[k] = 1

ans = []
for si in s2:
    if result[si] == -1:
        ans.append('Draw')
    elif result[si] == 1:
        ans.append('Takahashi')
    else:
        ans.append('Aoki')
print('\n'.join(ans))

