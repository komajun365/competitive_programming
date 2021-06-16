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
read = sys.stdin.buffer.read

n,*uvw = map(int,read().split())
mod = 10**9 + 7

links = [[] for _ in range(n)]
it = iter(uvw)
for u,v,w in zip(it,it,it):
    u -= 1
    v -= 1
    links[u].append([w,v])
    links[v].append([w,u])

stack = [0]
tp = []
parent = [[-1,-1] for _ in range(n)]
parent[0] = [0,0]
while stack:
    i = stack.pop()
    for w,j in links[i]:
        if parent[j][0] != -1:
            continue
        parent[j] = [i,w]
        stack.append(j)
        tp.append(j)

tp = tp[::-1]

res = [0] * 60
cnt = [[0] * 120 for _ in range(n)]
for i in tp:
    j,w = parent[i]
    for b in range(60):
        if w % 2 == 0:
            cnt_i = cnt[i][b*2:b*2+2]
            cnt_i[0] += 1
        else:
            cnt_i = cnt[i][b*2:b*2+2]
            cnt_i = cnt_i[::-1]
            cnt_i[1] += 1
        res[b] += cnt_i[1] + cnt_i[0] * cnt[j][b*2+1] + cnt_i[1] * cnt[j][b*2]
        cnt[j][b*2] += cnt_i[0]
        cnt[j][b*2+1] += cnt_i[1]
        w //= 2

ans = 0
for b in range(60):
    ans += res[b] * pow(2,b,mod)
    ans %= mod
print(ans)

# def calc(b):
#     res = 0
#     cnt = [[0,0] for _ in range(n)]
#     for i in tp:
#         j,w = parent[i]
#         w = (w>>b) & 1
#         if w == 0:
#             cnt_i = cnt[i]
#             cnt_i[0] += 1
#         else:
#             cnt_i = cnt[i][::-1]
#             cnt_i[1] += 1
#         res += cnt_i[1] + cnt_i[0] * cnt[j][1] + cnt_i[1] * cnt[j][0]
#         # res %= mod
#         cnt[j][0] += cnt_i[0]
#         cnt[j][1] += cnt_i[1]
#     res *= pow(2,b,mod)
#     res %= mod
#     # print(b, cnt)
#     return res

# ans = 0
# for b in range(60):
#     ans += calc(b)
#     ans %= mod
# print(ans)
        


