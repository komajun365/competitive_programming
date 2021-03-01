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

n,k,s,t = map(int,input().split())
a = list(map(int,input().split()))

fac = [1] * (n+1)
for i in range(1,n+1):
    fac[i] = fac[i-1] * i
com = [[0] * (n+1) for _ in range(n+1)]
for i in range(n+1):
    for j in range(i+1):
        com[i][j] = fac[i] // (fac[j] * fac[i-j])

com_n = [0] * (n+1)
for i in range(n+1):
    for j in range(1,k+1):
        com_n[i] += com[i][j]

mask = [-1] * 18
for i in range(18):
    si = (s >> i) & 1
    ti = (t >> i) & 1
    if si == 0 and ti == 0:
        mask[i] = 0
    elif si == 0 and ti == 1:
        mask[i] = 2
    elif si == 1 and ti == 0:
        print(0)
        exit()
    else:
        mask[i] = 1

b = []
for ai in a:
    tmp = 0
    for j in range(17,-1,-1):
        x = (ai >> j) & 1
        if mask[j] == 0 and x == 1:
            break
        if mask[j] == 1 and x == 0:
            break
        if mask[j] == 2:
            tmp = tmp*2 + x
    else:
        b.append(tmp)

l = mask.count(2)

ans = 0
for i in range(2**l):
    pc = bin(i).count('1')
    pm = (-1) ** pc
    cnt = dict()
    for bi in b:
        tmp = bi & i
        if tmp in cnt:
            cnt[tmp] += 1
        else:
            cnt[tmp] = 1
    
    for j in cnt.values():
        ans += pm * com_n[j]

print(ans)

# cnt_0 = [0] * (2**l)
# cnt_1 = [0] * (2**l)
# for bi in b:
#     j = bi
#     while( j >= 0):
#         cnt_1[j] += 1
#         # j==0ならbreak
#         if(j==0):
#             break
#         #jの更新
#         j = (j-1) & bi
#     bi = 2**l - 1 - bi
#     j = bi
#     while( j > 0):
#         cnt_0[j] += 1
#         #jの更新
#         j = (j-1) & bi

# ans = 0
# for i in range(2**l):
#     pc = bin(i).count('1')
#     pm = (-1) ** pc
#     for j in range(1,k+1):
#         ans += pm * com[cnt_0[i]][j]
#         ans += pm * com[cnt_1[i]][j]
#     print(i,ans)

# print(ans)
# print(b)

# print(cnt_0)
# print(cnt_1)