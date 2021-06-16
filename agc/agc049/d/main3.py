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

# 解説方針。戻すDP

n,m = map(int,input().split())
mod = 10**9 + 7
m0 = m

for h in range(n):
    if h * (h+1) // 2 > m:
        h -= 1
        break

dp = [0] * (m+1)
dp[0] = 1

def add(w):
    for i in range(m-w+1):
        dp[i+w] += dp[i]
        dp[i+w] %= mod
    # if w in items:
    #     items[w] += 1
    # else:
    #     items[w] = 1

def erase(w):
    for i in range(m-w,-1,-1):
        dp[i+w] -= dp[i]
        dp[i+w] %= mod
    # items[w] -= 1

# items = dict()

ans = 0
add(n)
for i in range(1,h+1):
    x = i*(i+1)//2
    add(x)

ans += dp[m]
ans %= mod

for l in range(1,h+1):
    r = n-l
    x = l*(l+1)//2
    m = m0 - x
    add(x)
    x = r*(r+1)//2
    erase(x)
    ans += dp[m]
    ans %= mod
    # print(l,r,ans)
    # print(dp)

print(ans)
