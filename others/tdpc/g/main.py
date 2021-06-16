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

# import array
# import gc

s = input()
k = int(input())
n = len(s)

idxs = [[-1] for _ in range(26)]
for i,si in enumerate(s):
    idxs[ord(si) - ord('a')].append(i)
for i in range(26):
    idxs[i].append(n)

ch_idx = [0] * 26
for i in range(26):
    ch_idx[i] = len(idxs[i]) - 1

inf = 10**18 + 5
dp = [1] * (n+1)
for i in range(n-1,-2,-1):
    for j in range(26):
        while ch_idx[j] > 0 and idxs[j][ch_idx[j]-1] > i:
            ch_idx[j] -= 1
        idx = idxs[j][ch_idx[j]]
        if idx == -1 or idx == n:
            continue
        dp[i] += dp[idx]
        if dp[i] >= inf:
            dp[i] = inf
            break

# print(dp)

if dp[-1]-1 < k:
    print('Eel')
    exit()

x = k
ans = ''
idx = -1
ch_idx = [0] * 26
while x > 0:
    for i in range(26):
        while idxs[i][ch_idx[i]] < n and idxs[i][ch_idx[i]] <= idx:
            ch_idx[i] += 1
        idx2 = idxs[i][ch_idx[i]]
        if idx2 == -1 or idx2 == n:
            continue
        # print(x,idx,idx2,ch_idx[i],idxs[i] )
        if dp[idx2] >= x:
            ans += chr(ord('a') + i)
            idx = idx2
            x -= 1
            break
        x -= dp[idx2]

print(ans)