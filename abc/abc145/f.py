# a,b = map(int,input().split())
# a = list(map(int,input().split()))
# a = [list(map(int,input().split())) for _ in range(n)]

import sys
import os
f = open('../../input.txt', 'r')
sys.stdin = f

n,k = map(int,input().split())
h = list(map(int,input().split()))

if(n==k):
    print(0)
    exit()

def calc(h_ind):
    hlen = len(h_ind)
    ans = h[h_ind[0]]
    for i in range(1,hlen):
        ans += max(h[h_ind[i]]-h[h_ind[i-1]], 0)

    return ans

inf = 10**9 * (n+1)
dp = [[inf] * (n-k+1) for _ in range(n+1)]
dp_element = []
for i in range(n+1):
    tmp = [[] for _ in range(n-k+1)]
    dp_element.append(tmp)
dp[0][0] = 0

for i in range(1,n+1):
    for j in range(1,n-k+1):
        # print('{} {}'.format(i,j))
        h_ind = dp_element[i-1][j-1][::]
        if(len(h_ind) != j-1):
            continue
        h_ind.append(i-1)
        tmp = calc(h_ind)
        if( dp[i-1][j] < tmp):
            dp[i][j] = dp[i-1][j]
            dp_element[i][j] = dp_element[i-1][j][::]
        elif(dp[i-1][j] == tmp):
            h_ind_b = dp_element[i-1][j][-1]
            h_ind_n = h_ind[-1]
            if(h[h_ind_b] < h[h_ind_n]):
                dp[i][j] = dp[i-1][j]
                dp_element[i][j] = dp_element[i-1][j][::]
            else:
                dp[i][j] = tmp
                dp_element[i][j] = h_ind[::]

        else:
            dp[i][j] = tmp
            dp_element[i][j] = h_ind[::]

print(dp[-1][-1])
# for i in dp_element:
#     print(i)
