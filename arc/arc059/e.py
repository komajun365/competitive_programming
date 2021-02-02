# a,b = map(int,input().split())
# a = list(map(int,input().split()))
# a = [list(map(int,input().split())) for _ in range(n)]

# import sys
# read = sys.stdin.buffer.read
# readline = sys.stdin.buffer.readline
# readlines = sys.stdin.buffer.readlines

# 検討?分　実装分 バグとり分

import sys
import os
f = open('../../input.txt', 'r')
sys.stdin = f

n,c = map(int,input().split())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
mod = 10**9+7

ex400 = [[1] * 401 for _ in range(401)]
for i in range(2,401):
    for j in range(1,401):
        ex400[i][j] = (ex400[i][j-1] * i) % mod

cumsum400 = [[1] * 401 for _ in range(401)]
for i in range(1,401):
    for j in range(401):
        cumsum400[i][j] = (cumsum400[i-1][j] + ex400[i][j]) % mod

dp = [[0] * (c+1) for _ in range(n+1)]
dp[0][0] = 1


for i in range(1,n+1):
    for j in range(c+1):
        for k in range(j+1):
            dp[i][j] += dp[i-1][j-k] * (cumsum400[b[i-1]][k] - cumsum400[a[i-1]-1][k])
            dp[i][j] %= mod

print(dp[-1][-1])





# for i in range(10):
#     tmp = cumsum400[i]
#     print(tmp[:10])




'''
i番目の子供が、キャンディーをj個もらえるのは
(c-j)個をn-1人に配る方法の組み合わせなので
(c-j+n-2)C(c-j)

dp[i][j] := i番目の子供に合計j個まで配ったときのうれしさの合計

dp[i+1][j] = dp[i][0] * xi**j + dp[i][1] * xi**(j-1) + ...


'''
