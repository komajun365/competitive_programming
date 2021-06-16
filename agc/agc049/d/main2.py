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

dp = [0] * ((m+1)*(h+2))
dp[0] = 1
# dp = [[0] * (m+1) for _ in range(h+2)]
# dp[0][0] = 1
for i in range(1,h+1):
    x = i * (i+1) //2
    for j in range(m+1):
        if j < x:
            dp[i*(m+1)+j] = dp[(i-1)*(m+1)+j]
        else:
            dp[i*(m+1)+j] = (dp[(i-1)*(m+1)+j] + dp[i*(m+1)+j-x]) % mod
      
ans = 0

for r in range(h+1):
    l = min(n-1-r, h)
    if l < 0:
        break

    for i in range(min(n,m+1)):
        l_sum = 0
        li = l*(m+1)+i
        limit = (l+1)*(m+1) - 1
        while li <= limit:
            l_sum += dp[li]
            l_sum %= mod
            li += n
            # print(li,l_sum)
        li -= n
        ri = limit - li + r*(m+1)
        # print(li,ri,limit,l*(m+1),l_sum)

        while li >= l*(m+1):
            ans += l_sum * (dp[ri] - dp[ri-(m+1)])
            ans %= mod
            l_sum -= dp[li]
            l_sum %= mod
            li -= n
            ri += n
        # print(l,r,i,ans)

print(ans)
# print(dp)



# for i in dp:
#     print(i)