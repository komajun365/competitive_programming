import numpy as np

n = int(input())
s = input()

# dp = np.zeros([n+1, n+1])
dp = [[0]*(n+1)] *(n+1)

for l1_r in range(1,n):
    for l2_r in range(l1_r+1, n+1):
        if(s[l1_r-1] == s[l2_r-1]):
            temp = dp[l1_r-1][l2_r-1]
            if( (l2_r - l1_r) > temp):
                  temp += 1
            dp[l1_r][l2_r] = temp

# print(int(dp.max()))

hoge = 0
