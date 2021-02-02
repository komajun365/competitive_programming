import sys
import os
f = open('../../input.txt', 'r')
sys.stdin = f

import numpy as np

s = input()
t = input()

dp = np.full(len(t) , '', dtype=object)
# dp_len = [0]* len(t)

for i in range(len(s)):
    s_temp = s[i]
    temp_max = ''
    max_len = 0
    for j in range(len(t)):
        before = dp[j]
        if(s_temp == t[j]):
            dp[j] = temp_max + s_temp
        if(max_len < len(before)):
            temp_max = before
            max_len = len(temp_max)

ans = ''
for j in range(len(t)):
    if(len(dp[j]) > len(ans)):
        ans = dp[j]

print(ans)
