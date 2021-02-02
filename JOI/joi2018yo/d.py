# a,b = map(int,input().split())
# a = list(map(int,input().split()))
# a = [list(map(int,input().split())) for _ in range(n)]

# import sys
# read = sys.stdin.buffer.read
# readline = sys.stdin.buffer.readline
# readlines = sys.stdin.buffer.readlines

# 検討24分　実装9分 バグとり15分

import sys
import os
f = open('../../input.txt', 'r')
sys.stdin = f

import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

N = int(readline())
L = list(map(int,read().split()))
cumsum = [0] * (N+1)
for i in range(N):
    cumsum[i+1] += cumsum[i] + L[i]

if(N==2):
    print(abs(L[1]-L[0]))
    exit()

ans = cumsum[-1]
for l in range(1,N):
    bef = []
    bef.append((l,cumsum[l], cumsum[l],0))
    for i in range(l+1,N+1):
        cand = []
        min_dif = cumsum[-1]
        for j,min_j,max_j,dif_j in bef:
            new = cumsum[i] - cumsum[j]
            min_new = min(min_j,new)
            max_new = max(max_j,new)
            dif_new = max_new - min_new
            if(min_dif >= dif_new):
                cand.append((i,min_new,max_new,dif_new))
                min_dif = dif_new
        if(i==N):
            ans = min(ans, min_dif)
            continue
        for j in cand:
            if(j[3]==min_dif):
                bef.append(j)

print(ans)


# for l in range(1,N):
#     dp = [[0,cumsum[-1]] for _ in range(N+1)]
#     dp[l] = [cumsum[l], cumsum[l]]
#     for i in range(l+1,N+1):
#         for j in range(l,i):
#             new = cumsum[i] - cumsum[j]
#             tmp = [0,0]
#             tmp[0] = min(dp[j][0], new)
#             tmp[1] = max(dp[j][1], new)
#             if( dp[i][1]-dp[i][0] > tmp[1] - tmp[0] ):
#                 dp[i] = tmp[::]
#     ans = min(ans, dp[-1][1]-dp[-1][0])

# print(ans)


'''
dpをN-1回繰り返す。
左端のようかんについて、L1-Llまでの長さを確保するとする。
以降、i>lについて、
dp[i] :=  適切に切ったときの[最小の長さのようかんの切れ端 , 最大の長さのようかんの切れ端]
とする。
累積和cumsum[i] := Liまでの累積和　として
下記で更新できる。
for j in range(l,i-1):
    new = cumsum[i] - cumsum[j]
    tmp = [0,0]
    tmp[0] = min(dp[i][0], new)
    tmp[1] = max(dp[i][1], new)
    if( dp[i][1]-dp[i][0] > tmp[1] - tmp[0] ):
        dp[i] = tmp[::]

dpの回数がO(N)
一回のdpの処理がO(N**2)
O(N**3）でいける？　本当か？

'''
