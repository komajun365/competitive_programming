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

a = input()

n = len(a)
b = []
base = ord('a')
for ai in a:
    b.append(ord(ai)-base)

right = [[n] * (n+1) for _ in range(26)]
for i,bi in enumerate(b):
    right[bi][i-1] = i

for i in range(26):
    for j in range(n-2, -2, -1):
        if right[i][j] == n:
            right[i][j] = right[i][j+1]

inf = 10**6
dp = [inf] * (n+1)
bef_idx = [0] * (n+1)
bef_chr = [26] * (n+1)
for i in range(n-1,-2,-1):
    for j in range(26):
        r = right[j][i]
        if r == n:
            dp[i] = 1
            bef_idx[i] = n
            bef_chr[i] = j
            break

        if dp[i] > dp[r] + 1:
            dp[i] = dp[r] + 1
            bef_idx[i] = r
            bef_chr[i] = b[r]

ans_s = []
idx = -1
while(idx < n):
    ans_s.append(bef_chr[idx])
    idx = bef_idx[idx]

ans = ''.join(map(lambda x: chr(x + base), ans_s))
print(ans)

# print(dp)
# print(bef_idx)
# print(bef_chr)

# for i in right:
#     print(i)

# left = [[-1] * (n+1) for _ in range(26)]
# for i,bi in enumerate(b):
#     left[bi][i+1] = i

# for i in range(26):
#     for j in range(1,n+1):
#         if left[i][j] == -1:
#             left[i][j] = left[i][j-1]

# inf = 10**6
# dp = [inf] * (n+1)
# bef_idx = [0] * (n+1)
# bef_chr = [26] * (n+1)
# for i in range(26):
#     for j in range(26):
#         l = left[j][n]
#         if l == -1:
#             print(chr(j + base))
#             exit()
#         if dp[l] > 1:
#             dp[l] = 1
#             bef_idx[l] = n
#             bef_chr[l] = i
#         elif dp[l] == 1:
#             if bef_chr[l] > i:
#                 bef_idx[l] = n
#                 bef_chr[l] = i

# for i in range(n-1,-1,-1):
#     for j in range(26):
#         l = left[j][i]
#         if dp[l] > dp[i] + 1:
#             dp[l] = dp[i] + 1
#             bef_idx[l] = i
#             bef_chr[l] = b[i]
#         elif dp[l] == dp[i] + 1:
#             if bef_chr[l] > b[i]:
#                 bef_idx[l] = i
#                 bef_chr[l] = b[i]

# ans_s = []
# idx = -1
# while(idx < n):
#     ans_s.append(bef_chr[idx])
#     idx = bef_idx[idx]

# ans = ''.join(map(lambda x: chr(x + base), ans_s))
# print(ans)

# print(dp)
# print(bef_idx)
# print(bef_chr)

# for i in range(-1,n):
#     print(i,dp[i],bef_idx[i],chr(bef_chr[i] + base))


# frqnvhydsc
# shfcgdemur
# lfrutcpzho
# pfotpifgep
# nqjxupnska
# pziurswqaz
# dwnwbgdhyk
# tfyhqqxpoi
# dfhjdakoxr
# aiedxskywu
# epzfniuysk
# xiyjpjlxuq
# nfgmnjcvtl
# pnclfkperv
# xmdbvrbrdn


# [3, 3, 3, 3, 2, 4, 3, 4, 4, 4,
#  3, 3, 3, 3, 3, 3, 3, 2, 3, 3, 
#  2, 3, 3, 3, 3, 2, 4, 3, 3, 4, 
#  4, 4, 3, 3, 3, 3, 3, 3, 2, 3, 
#  3, 3, 2, 3, 3, 4, 3, 3, 3, 3, 
#  3, 3, 3, 2, 2, 2, 3, 3, 2, 2, 
#  3, 3, 2, 2, 2, 2, 3, 3, 3, 2, 
#  2, 3, 2, 2, 3, 2, 2, 2, 2, 2, 
#  2, 2, 1, 2, 2, 2, 2, 1, 2, 2, 
#  1, 2, 2, 2, 2, 2, 2, 2, 1, 2, 
#  2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 
#  2, 1, 1, 3, 2, 2, 2, 2, 1, 1, 
#  2, 2, 1, 2, 2, 1, 2, 2, 1, 2, 
#  2, 2, 1, 1, 1, 1, 1, 1, 2, 2, 
#  1, 1, 2, 2, 1, 2, 1, 1, 1, 1, 3]\r

# [4, 17, 25, 25, 90, 11, 58, 13, 10, 13,
#  25, 25, 20, 25, 25, 58, 25, 90, 20, 20, 
#  90, 25, 25, 25, 25, 90, 28, 38, 58, 32, 
#  32, 36, 58, 58, 38, 38, 58, 58, 90, 42, 
#  42, 42, 82, 58, 53, 49, 58, 54, 58, 58, 
#  58, 58, 58, 90, 82, 90, 58, 58, 82, 90, 
#  64, 62, 90, 90, 90, 90, 80, 73, 69, 82, 
#  90, 80, 90, 82, 75, 90, 82, 90, 82, 90, 
#  82, 90, 150, 90, 90, 90, 90, 150, 90, 90, 
#  150, 98, 98, 132, 108, 108, 108, 98, 150, 102, 
#  132, 111, 150, 111, 111, 111, 111, 111, 150, 132, 
#  111, 150, 150, 115, 122, 122, 122, 132, 150, 150, 
#  122, 132, 150, 132, 125, 150, 132, 132, 150, 132,
#  132, 146, 150, 150, 150, 150, 150, 150, 141, 141, 
#  150, 150, 146, 146, 150, 146, 150, 150, 150, 150, 58]\r

# [21, 12, 2, 2, 0, 7, 0, 2, 18, 2, 2, 2, 11, 2, 2, 0, 2, 0, 11, 11, 0, 2, 2, 2, 2, 0, 7, 4, 0, 14, 14, 5, 0, 0, 4, 4, 0, 0, 0, 9, 9, 9, 7, 0, 20, 0, 0, 17, 0, 0, 0, 0, 0, 0, 7, 0, 0, 0, 7, 0, 1, 13, 0, 0, 0, 0, 3, 7, 10, 7, 0, 3, 0, 7, 16, 0, 7, 0, 7, 0, 7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 22, 22, 2, 18, 18, 18, 22, 0, 25, 2, 8, 0, 8, 8, 
# 8, 8, 8, 0, 2, 8, 0, 0, 9, 6, 6, 6, 2, 0, 0, 6, 2, 0, 2, 9, 0, 2, 2, 0, 2, 2, 1, 0, 0, 0, 0, 0, 0, 12, 12, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0]\r