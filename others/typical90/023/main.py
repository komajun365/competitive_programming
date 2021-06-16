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

h,w,*s = read().split()
h = int(h)
w = int(w)
mod = 10**9 + 7

can = set()
for i in range(1<<w):
    for j in range(w-1):
        if (i >> j) & 3 == 3:
            break
    else:
        can.add(i)

can = list(can)
encode = dict()
for i,ci in enumerate(can):
    encode[ci] = i

l = len(can)
after = [[] for _ in range(l)]



for i in can:
    j = i
    while j >= 0:
        dif = i ^ j
        j_ind = encode[j]
        d_ind = encode[dif]
        after[j_ind].append(d_ind)

        # j==0ならbreak
        if(j==0):
            break
        #jの更新
        j = (j-1) & i

# tot = 0
# for i in after:
#     tot += len(i)
# print(l)
# print(tot)

dp = [0] * l
dp[encode[0]] = 1

for si in s:
    sb = 0
    for c in si:
        sb *= 2
        sb += 1 * (c=='#')
    
    dp2 = [0] * l
    for i in range(l):
        if dp[i] == 0:
            continue
        for cand in after[i]:
            if can[cand] & sb:
                continue
            dp2[cand] += dp[i]
            dp2[cand] %= mod

    dp,dp2 = dp2,dp
    # print(dp)

ans = sum(dp) % mod
print(ans)
# print(after)
# print(can)


# can = list(can)
# can.sort()

# def calc(x):
#     gr = set()
#     gr.add(x)
#     stack = [x]
#     while stack:
#         i = stack.pop()
#         for j in range(w):
#             if (i >> j) & 1:
#                 continue
#             k = i | (1<<j)
#             if not k in cnt:
#                 continue
#             if k in gr:
#                 continue
#             gr.add(k)
#             stack.append(k)
    
#     return len(gr)