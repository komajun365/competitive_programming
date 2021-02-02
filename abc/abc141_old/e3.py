# import numpy as np

n = int(input())
s = input()

# dp = np.zeros([n+1, n+1])
dp = [0] * (n+1)

for dif in range(1,n):
    count = 0
    t_max = 0
    for l1_r in range(0, n-dif):
        if(s[l1_r] == s[l1_r + dif]):
            count += 1
            t_max = max(count, t_max)
            if( count == dif):
                dp[dif] = count
                break
        else:
            count = 0
    dp[dif] = t_max

print(max(dp))    
