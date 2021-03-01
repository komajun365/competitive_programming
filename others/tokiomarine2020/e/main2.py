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

# ブログ用に清書

n,k,s,t = map(int,input().split())
a = list(map(int,input().split()))

# 二項係数の事前計算
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

# 要らない数、桁の圧縮
use = [-1] * 18
for i in range(18):
    si = (s >> i) & 1
    ti = (t >> i) & 1
    if si == 0 and ti == 0:
        use[i] = 0
    elif si == 0 and ti == 1:
        use[i] = 2
    elif si == 1 and ti == 0:
        print(0)
        exit()
    else:
        use[i] = 1

a2 = []
for ai in a:
    new = 0
    for j in range(17,-1,-1):
        x = (ai >> j) & 1
        if use[j] == 0 and x == 1:
            break
        if use[j] == 1 and x == 0:
            break
        if use[j] == 2:
            new = new*2 + x
    else:
        a2.append(new)

# 包除原理で数え上げ
l = use.count(2) # 圧縮後の桁数
ans = 0
for mask in range(2**l):
    group_cnt = dict()
    for ai in a2:
        masked = ai & mask
        if masked in group_cnt:
            group_cnt[masked] += 1
        else:
            group_cnt[masked] = 1

    pc = bin(mask).count('1')    
    for j in group_cnt.values():
        ans += (-1) ** pc * com_n[j]

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