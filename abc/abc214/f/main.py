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

s = input()
mod = 10**9 + 7
n = len(s)

idx = [[] for _ in range(26)]
for i in range(n):
    si = s[i]
    idx[ord(si) - ord('a')].append(i)

dp = [0] * n
cand = [0] * 26
for i in range(26):
    if idx[i]:
        dp[idx[i][0]] += 1

ans = 0
for i in range(n):
    for j in range(26):
        # print(j,cand,idx)
        if cand[j] == len(idx[j]):
            continue
        target = idx[j][cand[j]]
        while target <= i+1:
            cand[j] += 1
            if cand[j] == len(idx[j]):
                break
            target = idx[j][cand[j]]
        if cand[j] == len(idx[j]):
            continue

        dp[target] += dp[i]
        dp[target] %= mod
    ans += dp[i]
    ans %= mod

print(ans)
        



