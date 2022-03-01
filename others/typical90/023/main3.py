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

if w == 1:
    dp = [1,0]
    for i in range(h):
        if s[i][0] == '.':
            dp2 = [sum(dp)%mod, dp[0]]
        else:
            dp2 = [sum(dp)%mod, 0]
        dp,dp2 = dp2,dp
    ans = sum(dp) % mod
    print(ans)
    exit()

state0 = [0,1]
state1 = []
for i in range(w):
    state02 = []
    state12 = []
    for j in state0:
        state02.append(j<<1)
        if j&1 == 0:
            state02.append((j<<1) + 1)
        else:
            state12.append((j<<1) + 1)
    for j in state1:
        state12.append(j<<1)
        if j&1 == 0:
            state12.append((j<<1) + 1)
    state0,state02 = state02,state0
    state1,state12 = state12,state1

state = state0 + state1
encode = {si:i  for i,si in enumerate(state)}

base = (1 << (w+1)) - 1
next_ = []
next_left = []
next_right = []
next_others = []
for si in state:
    next_num = (si << 1) & base
    next0 = encode[next_num]
    next1 = encode.get(next_num+1,-1)
    next_.append([next0])
    next_left.append([next0])
    next_right.append([next0])
    next_others.append([next0])
    # 左端
    if (si >> (w-1))& 1 == 0 and (si >> (w-2))& 1 == 0:
        next_left[-1].append(next1)
    # 右端
    if (si >> w)& 1 == 0 and (si >> (w-1))& 1 == 0 and (si&1) == 0:
        next_right[-1].append(next1)
    # 両端以外
    if (si >> w)& 1 == 0 and (si >> (w-1))& 1 == 0 and \
        (si >> (w-2))& 1 == 0 and (si&1) == 0:
        next_others[-1].append(next1)

m = len(state)
dp = [0] * m
dp[encode[0]] = 1
for i in range(h):
    for j in range(w):
        dp2 = [0] * m
        if s[i][j] == '#':
            for k in range(m):
                for l in next_[k]:
                    dp2[l] += dp[k]
                    dp2[l] %= mod
        elif j == 0:
            for k in range(m):
                for l in next_left[k]:
                    dp2[l] += dp[k]
                    dp2[l] %= mod
        elif j == w-1:
            for k in range(m):
                for l in next_right[k]:
                    dp2[l] += dp[k]
                    dp2[l] %= mod
        else:
            for k in range(m):
                for l in next_others[k]:
                    dp2[l] += dp[k]
                    dp2[l] %= mod
        dp,dp2 = dp2,dp

ans = sum(dp) % mod
print(ans)

# base = (1 << (w+1)) - 1
# cnt = dict()
# cnt[0] = 1
# for i in range(h):
#     for j in range(w):
#         cnt2 = dict()
#         flag = s[i][j] == '.'
#         for k,v in cnt.items():
#             k1 = (k << 1) & base
#             cnt2[k1] = (cnt2.get(k1,0) + v) % mod
#             if flag:
#                 # 左端
#                 if j == 0:
#                     if (k >> (w-1))& 1 == 0 and (k >> (w-2))& 1 == 0:
#                         cnt2[k1+1] = (cnt2.get(k1+1,0) + v) % mod
#                 # 右端
#                 elif j == w-1:
#                     if (k >> w)& 1 == 0 and (k >> (w-1))& 1 == 0 and (k&1) == 0:
#                         cnt2[k1+1] = (cnt2.get(k1+1,0) + v) % mod
#                 # 両端以外
#                 else:
#                     if (k >> w)& 1 == 0 and (k >> (w-1))& 1 == 0 and \
#                         (k >> (w-2))& 1 == 0 and (k&1) == 0:
#                         cnt2[k1+1] = (cnt2.get(k1+1,0) + v) % mod

#         cnt,cnt2 = cnt2,cnt

# ans = 0
# for v in cnt.values():
#     ans += v
#     ans %= mod
# print(ans)




