import sys
import os
f = open('../../input.txt', 'r')
sys.stdin = f

s = input()
t = input()

s_len = len(s)
t_len = len(t)

dp = [[0] * (t_len+1) for _ in range(s_len+1)]

for i in range(1,s_len+1):
    s_temp = s[i-1]
    for j in range(1, t_len+1):
        if(s_temp == t[j-1]):
            dp[i][j] = max(dp[i-1][j], dp[i][j-1], dp[i-1][j-1] + 1)
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])

ans = ''
while(s_len > 0 and t_len > 0):
    if(dp[s_len][t_len] == dp[s_len-1][t_len]):
        s_len -= 1
    elif(dp[s_len][t_len] == dp[s_len][t_len-1]):
        t_len -= 1
    else:
        ans = s[s_len-1]  + ans
        s_len -= 1
        t_len -= 1

print(ans)
