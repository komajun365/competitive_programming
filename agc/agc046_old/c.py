# a,b = map(int,input().split())
# a = list(map(int,input().split()))
# a = [list(map(int,input().split())) for _ in range(n)]

# import sys
# read = sys.stdin.buffer.read
# readline = sys.stdin.buffer.readline
# readlines = sys.stdin.buffer.readlines

# 検討?分　実装分 バグとり分

import sys
import os
f = open('../../input.txt', 'r')
sys.stdin = f

sk = input().split()
s = sk[0]
k = int(sk[1])

n = s.count('1')
cnt = [0]
for si in s:
    if(si=='0'):
        cnt.append(0)
    else:
        cnt[-1]+=1

print(cnt)
print(n)
dp = [[0] * (n+1) for _ in range(len(cnt))]



'''
ストックとコストで考える
dp[x][i][j] := -xまで確認した時に、現在コストi払っていて、j個のストックがある状態、とする。

cnt[-x] = yとしたときに、
・
dp[x+1][i][j] = dp[x][i-y][j-y] +
                dp[x][i-y+1][j-y+1] +
                dp[x][i-y+2][j-y+2] +
                :
                dp[x][i][j] +
                dp[x][i][j-1] +
                dp[x][i][j-2] +
                :
                dp[x][i][0]




'''
