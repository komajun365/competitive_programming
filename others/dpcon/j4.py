import sys
import os
f = open('../../input.txt', 'r')
sys.stdin = f

n = int(input())
a = input().split()

c1 = a.count('1')
c2 = a.count('2')
c3 = a.count('3')

dp =[ [[0] * (n+1) for _ in range(c3+c2+1)] for __ in range(c3+1)]
# dp[0][0][0] = 0

for i in range(c3+1):
    for j in range(c3+c2+1-i):
        for k in range(n+1-i-j):
            if(i+j+k == 0):
                dp[i][j][k]=0
            else:
                temp = 0
                if(i > 0):
                    temp += dp[i-1][j+1][k] * i/(k+j+i)
                if(j > 0):
                    temp += dp[i][j-1][k+1] * j/(k+j+i)
                if(k > 0):
                    temp += dp[i][j][k-1] * k/(k+j+i)
                dp[i][j][k] = temp + n/(k+j+i)

print(dp[c3][c2][c1])


# def calc_dp(i,t2,t1):
#     global dp
#     if(dp[t3][t2][t1] > -1):
#         return dp[t3][t2][t1]
#
#     temp = 0
#     if(t3 > 0):
#         temp += calc_dp(t3-1,t2+1,t1) * t3/(t1+t2+t3)
#     if(t2 > 0):
#         temp += calc_dp(t3,t2-1,t1+1) * t2/(t1+t2+t3)
#     if(t1 > 0):
#         temp += calc_dp(t3,t2,t1-1) * t1/(t1+t2+t3)
#     temp = temp + n/(t1+t2+t3)
#
#     dp[t3][t2][t1] = temp
#     return temp
#
# print(calc_dp(c3,c2,c1))
