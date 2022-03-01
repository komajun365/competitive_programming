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

base = (1 << (w+1)) - 1
mask_left = (1<<(w-1)) + (1<<(w-2))
mask_right = (1<<(w)) + (1<<(w-1)) + 1
mask_others = (1<<(w)) + (1<<(w-1)) + (1<<(w-2)) + 1
cnt = dict()
cnt[0] = 1

for i in range(h):
    for j in range(w):
        cnt2 = dict()
        if s[i][j] == '#':
            for k,v in cnt.items():
                v %= mod
                k1 = (k << 1) & base
                cnt2[k1] = (cnt2.get(k1,0) + v)
        # 左端
        elif j == 0:
            for k,v in cnt.items():
                v %= mod
                k1 = (k << 1) & base
                cnt2[k1] = (cnt2.get(k1,0) + v)
                if k & mask_left == 0:
                    cnt2[k1+1] = (cnt2.get(k1+1,0) + v)
        # 右端
        elif j == w-1:
            for k,v in cnt.items():
                v %= mod
                k1 = (k << 1) & base
                cnt2[k1] = (cnt2.get(k1,0) + v)
                if k & mask_right == 0:
                    cnt2[k1+1] = (cnt2.get(k1+1,0) + v)
        # 両端以外
        else:
            for k,v in cnt.items():
                v %= mod
                k1 = (k << 1) & base
                cnt2[k1] = (cnt2.get(k1,0) + v)
                if k & mask_others == 0:
                    cnt2[k1+1] = (cnt2.get(k1+1,0) + v)
                    
        cnt,cnt2 = cnt2,cnt

ans = 0
for v in cnt.values():
    ans += v
    ans %= mod
print(ans)




# for i in range(h):
#     for j in range(w):
#         cnt2 = dict()
#         flag = s[i][j] == '.'
#         for k,v in cnt.items():
#             v %= mod
#             k1 = (k << 1) & base
#             cnt2[k1] = (cnt2.get(k1,0) + v)

#             if flag:
#                 # 左端
#                 if j == 0:
#                     if k & mask_left == 0:
#                         cnt2[k1+1] = (cnt2.get(k1+1,0) + v)
#                 # 右端
#                 elif j == w-1:
#                     if k & mask_right == 0:
#                         cnt2[k1+1] = (cnt2.get(k1+1,0) + v)
#                 # 両端以外
#                 else:
#                     if k & mask_others == 0:
#                         cnt2[k1+1] = (cnt2.get(k1+1,0) + v)

#         cnt,cnt2 = cnt2,cnt

# ans = 0
# for v in cnt.values():
#     ans += v
#     ans %= mod
# print(ans)




