# oj t -c "python main.py" -d "./tests/" 

# a,b = map(int,input().split())
# a = list(map(int,input().split()))
# a = [list(map(int,input().split())) for _ in range(n)]

# import sys
# read = sys.stdin.buffer.read
# readline = sys.stdin.buffer.readline
# readlines = sys.stdin.buffer.readlines

# 検討?分　実装分 バグとり分

# import sys
# import os
# f = open('../../../input.txt', 'r')
# sys.stdin = f

import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
import bisect

n,d,k,*ps = map(int,read().split())

inf = 10**13
event= [[inf],[inf]]
it = iter(ps)
for p,s in zip(it,it):
    p -= 1
    event[p].append(s)
event[0].sort()
event[1].sort()

dp = [[-1] * (n+1) for _ in range(2)]
dp[0][0] = 0
dp[1][0] = 0

for i in range(1,n+1):
    next0 = event[0][bisect.bisect_left(event[0],dp[0][i-1])] + 1
    next1 = event[1][bisect.bisect_left(event[1],dp[1][i-1])] + 1
    if(next0 == next1 == inf+1):
        print(i-1)
        exit()
    if(next0 < next1):
        dp[0][i] = next0
        dp[1][i] = min(next1, dp[0][i] + d + k*i)
    else:
        dp[1][i] = next1
        dp[0][i] = min(next0, dp[1][i] + d + k*i)

print(n)
    
    





'''
dp[i][j] := i町にいて、j個イベントに参加した時の最短時間

dp[i][j] = min(dp[not i][j] + d+k*j, next(dp[i][j-1])+1)

'''