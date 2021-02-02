# a,b = map(int,input().split())
# a = list(map(int,input().split()))
# a = [list(map(int,input().split())) for _ in range(n)]

import sys
import os
f = open('../../input.txt', 'r')
sys.stdin = f

n,k = map(int,input().split())
r,s,p = map(int,input().split())
t = input()

def calc_dp(st):
    len_st = len(st)
    dp = [[0] * 3 for _ in range(len_st + 1)]
    for ind, i in enumerate(st, 1):
        dp[ind][0] = max(dp[ind-1][1],dp[ind-1][2])
        dp[ind][1] = max(dp[ind-1][0],dp[ind-1][2])
        dp[ind][2] = max(dp[ind-1][0],dp[ind-1][1])
        if(i=='r'):
            dp[ind][2] += p
        elif(i=='s'):
            dp[ind][0] += r
        else:
            dp[ind][1] += s

    return max(dp[-1])

ans = 0
for i in range( k ):
    if( i >= n ):
        break
    st = t[i::k]
    ans += calc_dp(st)

print(ans)
