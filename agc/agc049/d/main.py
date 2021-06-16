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

n,m = map(int,input().split())
mod = 10**9 + 7

for h in range(n+1):
    if h * (h+1) // 2 > m:
        h -= 1
        break

dp = [[0] * (m+1) for _ in range(h+2)]
dp[0][0] = 1
for i in range(1,h+1):
    x = i * (i+1) //2
    for j in range(m+1):
        if j < x:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = (dp[i-1][j] + dp[i][j-x]) % mod
      
ans = 0

for r in range(h+1):
    l = min(n-1-r, h)
    if l < 0:
        continue

    l_num = dp[l]

    for i in range(n):
        l_sum = 0
        li = i
        while li <= m:
            l_sum += l_num[li]
            l_sum %= mod
            li += n
        li -= n
        ri = m-li

        while li >= 0:
            ans += l_sum * (dp[r][ri] - dp[r-1][ri])
            ans %= mod
            l_sum -= l_num[li]
            l_sum %= mod
            li -= n
            ri += n
    # print(l,r,ans)

print(ans)




# for i in dp:
#     print(i)