# a,b = map(int,input().split())
# a = list(map(int,input().split()))
# a = [list(map(int,input().split())) for _ in range(n)]

# import sys
# read = sys.stdin.buffer.read
# readline = sys.stdin.buffer.readline
# readlines = sys.stdin.buffer.readlines

# 検討?分　実装分 バグとり分

import sys
import os
f = open('../../input.txt', 'r')
sys.stdin = f

import sys
read = sys.stdin.buffer.read

n,m,*data = map(int,read().split())
pq = data[:2*n]
rs = data[2*n:]

links_j = [[] for _ in range(n)]
links_i = [[] for _ in range(n)]
root_j = -1
root_i = -1
for i in range(n):
    p,q = pq[i*2:i*2+2]
    p -= 1
    q -= 1
    if p != -1:
        links_j[p].append(i)
    else:
        root_j = i
    if q != -1:
        links_i[q].append(i)
    else:
        root_i = i

dp = [[0] * n for _ in range(n)]
it = iter(rs)
for r,s in zip(it,it):
    r -= 1
    s -= 1
    dp[s][r] += 1

stack = [root_i]
while(stack):
    i = stack.pop()
    for j in links_i[i]:
        stack.append(j)
        for k in range(n):
            dp[j][k] += dp[i][k]

stack = [root_j]
while(stack):
    i = stack.pop()
    for j in links_j[i]:
        stack.append(j)
        for k in range(n):
            dp[k][j] += dp[k][i]

ans = []
for i in range(n):
    ans.append(dp[i][i])

print('\n'.join(map(str,ans)))

# print(dp)




# def calc(links):
#     res = []
#     for i in range(n):
#         d = [0] * n
#         d[i] = 1
#         stack = [i]
#         while(stack):
#             j = stack.pop()
#             for k in links[j]:
#                 if d[k] != 0:
#                     continue
#                 d[k] = 1
#                 stack.append(k)
#         res.append(d[:])
#     return res

# dj = calc(links_j)
# di = calc(links_i)

# ans = [0] * n
# it = iter(rs)
# for r,s in zip(it,it):
#     r -= 1
#     s -= 1
#     for i in range(n):
#         ans[i] += dj[i][r] * di[i][s]


# print(ans)


# links = [[] for _ in range(n*2)]
# for i in range(n):
#     p,q = pq[i*2:i*2+2]
#     p -= 1
#     q -= 1
#     if p != -1:
#         links[i].append(p)
#     if q != -1:
#         links[q+n].append(i+n)
#     links[i+n].append(i)

# d = []
# for i in range(n):
#     di = [0] * (2*n)
#     di[i+n] = 1
#     stack = [i+n]
#     while(stack):
#         j = stack.pop()
#         for k in links[j]:
#             if di[k] != 0:
#                 continue
#             di[k] = 1
#             stack.append(k)
#     d.append(di[:n])

# ans = [0] * n
# it = iter(rs)
# for r,s in zip(it,it):
#     r -= 1
#     s -= 1
#     stack = [s+n]
#     while(stack):
#         i = stack.pop()
#         print(i-n,r,d[i-n][r])
#         ans[i-n] += d[i-n][r]
#         for j in links[i]:
#             if j < n:
#                 continue
#             stack.append(j)

# print(ans)





'''


'''
