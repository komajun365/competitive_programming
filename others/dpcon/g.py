import sys
import os
f = open('../../input.txt', 'r')
sys.stdin = f

from sys import setrecursionlimit
setrecursionlimit(10 ** 7)

n, m = map(int, input().split())

xy_dict = {}
for i in range(1,n+1):
    xy_dict[i] = []

for i in range(m):
    x,y = map(int, input().split())
    xy_dict[x].append(y)

dp = [-1]*(n+1)
dp[0] = 0

def get_longest(x):
    global dp

    if( dp[x] >= 0):
        return dp[x]
    else:
        y_list = xy_dict[x]
        temp_max = 0
        for y in y_list:
            temp_max = max(temp_max, get_longest(y)+1)

        dp[x] = temp_max
        return temp_max

ans = 0
for i in range(1,n+1):
    ans = max(ans, get_longest(i))

print(ans)
