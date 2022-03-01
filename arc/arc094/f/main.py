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

change = {'ab':'cc', 'ba':'cc',
          'ac':'bb', 'ca':'bb',
          'bc':'aa', 'cb':'aa'}

def solve(s):
    l = len(s)
    done = set()
    done.add(s)
    stack = [s]
    while stack:
        x = stack.pop()
        for i in range(l-1):
            if x[i] == x[i+1]:
                continue
            y = x[:i] + change[x[i:i+2]] + x[i+2:]
            if not y in done:
                done.add(y)
                stack.append(y)
    
    return len(done)

s = input()
mod = 998244353
l = len(s)

if l < 4:
    print(solve(s))
    exit()

same = 0
for i in range(l-1):
    if s[i] == s[i+1]:
        same += 1

if same == l-1:
    print(1)
    exit()

tot = 0
for si in s:
    tot += ord(si) - ord('a')
tot %= 3

dp = [[0] * 3 for _ in range(3)]
dp[0][0] = 1
dp[1][1] = 1
dp[2][2] = 1
for _ in range(l-1):
    dp2 = [[0] * 3 for _ in range(3)]
    for i in range(3):
        for j in range(3):
            for k in range(3):
                if j == k:
                    continue
                dp2[(i+k) % 3][k] += dp[i][j]
                dp2[(i+k) % 3][k] %= mod
    dp,dp2 = dp2,dp

ans = (same == 0) + pow(3,l-1,mod) - sum(dp[tot])
ans %= mod
print(ans)




