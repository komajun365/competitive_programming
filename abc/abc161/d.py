# a,b = map(int,input().split())
# a = list(map(int,input().split()))
# a = [list(map(int,input().split())) for _ in range(n)]

import sys
import os
f = open('../../input.txt', 'r')
sys.stdin = f

k = int(input())

def calc(n):
    s = str(n)
    s_len = len(s)
    dp = [[0] * 12 for _ in range(s_len)]
    dp_o = [[0] * 12 for _ in range(s_len)]
    for i in range(1,int(s[0])):
        dp[0][i+1] = 1
    dp_o[0][int(s[0])+1] = 1

    for i in range(0,s_len-1):
        dp[i+1][1] = dp[i][1] + dp[i][2] + 1
        for k in range(2,11):
            dp[i+1][k] = dp[i][k-1] + dp[i][k] +dp[i][k+1] + 1
        dp[i+1][1] -= 1

        if(i != s_len-1):
            j_b = int(s[i])
            j_n = int(s[i+1])
            for j in range( max(0,j_b-1), min(9,j_b+1)+1  ):
                if( j < j_n):
                    dp[i+1][j+1] += dp[i][j_b+1]
            if(abs(j_n-j_b)<=1):
                dp_o[i+1][j_n+1] += dp_o[i][j_b+1]
    ans = 0
    for i in range(12):
        ans += dp[-1][i] + dp_o[-1][i]

    for tmp in dp:
        print(tmp)
    for tmp in dp_o:
        print(tmp)

    # print(dp)
    # print(dp_o)

    return ans

print(calc(3234566667))
