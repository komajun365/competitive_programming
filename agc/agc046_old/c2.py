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

sk = input().split()
s = sk[0]
K = int(sk[1])
mod = 998244353

x = [0]
for si in s:
    if(si=='0'):
        x.append(0)
    else:
        x[-1] += 1

while(x):
    if(x[-1] == 0):
        x.pop()
    else:
        break
x = x[::-1]
len_x = len(x)
ones = min(K,sum(x))
dp = [[] for _ in range(len_x+1)]

for i in range(len_x+1):
    dp[i] = [[0] * (ones+1) for _ in range(ones+1)]

dp[0][0][0] = 1
for i,xi in enumerate(x):
    cumsum_y = [[0] * (ones+2) for _ in range(ones+2)]
    cumsum_xy = [[0] * (ones+2) for _ in range(ones+2)]

    for j in range(ones+1):
        for k in range(ones+1):
            cumsum_y[j+1][k+1] = (cumsum_y[j][k+1] + dp[i][j][k])%mod
            cumsum_xy[j+1][k+1] = (cumsum_xy[j][k] + dp[i][j][k])%mod

    for j in range(ones+1):
        for k in range(j,ones+1):
            dp[i+1][j][k] += cumsum_y[k+1][k+1] - cumsum_y[j][k+1]
            dp[i+1][j][k] += cumsum_xy[j][k] - cumsum_xy[max(0,j-xi)][max(0,j-xi) + k-j]
            dp[i+1][j][k] %= mod

ans = 0
for k in range(ones+1):
    ans += dp[-1][0][k]
    ans %= mod

print(ans)
# print(x)

# for i in dp:
#     print(i)


'''
1の数をn
0の前に並ぶ1の数を数えて、
初期値x = [x1,x2,x3,...]を置く。

後ろから考えるとして、
dp[i][j][k] := i個目まで考えて、今ストックしている1の数がj個で、ここまでに回収した1の総数がk個

dp[i][j][k] = dp[i-1][j][k]
                + dp[i-1][j-1][k-1] + ... + dp[i-1][j-xi][k-xi]
                + dp[i-1][j+1][k] + ... + dp[i-1][k][k]


'''
