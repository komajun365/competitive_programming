# a,b = map(int,input().split())
# a = list(map(int,input().split()))
# a = [list(map(int,input().split())) for _ in range(n)]

import sys
import os
f = open('../../input.txt', 'r')
sys.stdin = f

k = int(input())

def calc_dp(n):
    if(n==0):
        return 0

    s = str(n)
    slen = len(s)
    dp = [[0] * 12 for _ in range(slen)]
    dp_o = [[0] * 12 for _ in range(slen)]

    #initial
    for i in range(1,int(s[0])):
        dp[0][i+1] = 1
    dp_o[0][int(s[0])+1] = 1

    #update
    for i in range(slen-1):
        for j in range(1,11):
            dp[i+1][j] = dp[i][j-1] + dp[i][j] + dp[i][j+1] +1
        dp[i+1][1] -= 1

        s_b = int(s[i])
        s_n = int(s[i+1])

        for j in range( max(0,s_b-1), min(10, s_b+2)  ):
            if(j < s_n ):
                dp[i+1][j+1] += dp_o[i][s_b+1]
            elif(j == s_n):
                dp_o[i+1][j+1] += dp_o[i][s_b+1]

    ans = 0
    for i in range(1,11):
        ans += dp[-1][i] + dp_o[-1][i]

    return ans

min_ = 0
max_ = 3234566676


for i in range(100):
    tmp = (min_+max_)//2
    tmp_c = calc_dp(tmp)
    if(k > tmp_c):
        min_ = tmp
    else:
        max_ = tmp

    if(max_ - min_ == 1 ):
        break

print(max_)
