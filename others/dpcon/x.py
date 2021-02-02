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

import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

n = int(readline())
wsv = [list(map(int,readline().split())) for _ in range(n)]
wsv.sort(key=lambda x:x[0]+x[1])

dp = [[0] * (2*10**4+1) for _ in range(n+1)]
for i in range(n):
    wi,si,vi = wsv[i]
    for j in range(1,2*10**4+1):
        if(j < wi):
            dp[i+1][j] = max(dp[i+1][j-1],dp[i][j])
        elif(j <= wi+si):
            dp[i+1][j] = max(dp[i+1][j-1],dp[i][j],dp[i][j-wi]+vi)
        else:
            dp[i+1][j] = max(dp[i+1][j-1],dp[i][j])

print(dp[-1][-1])
# for i in dp:
#     print(i[:10])


'''

dp[i][j] := i個目までのブロックを見て、重さj以下の価値最大値

w+sでソートしておきたい？


w,s=(1,10)
w,s=(8,8)
w,s(7,7)


w,s=10,2
w,s=3,6

w0
w1,s1
w2,s2

・もし0-1-2が積めていて、(w1+s1)>=(w2+s2)だったら
w0<=s1 , w0+w1<=s2

s1+s2 >= w1+s1+w0 >= w2+s2+w0
s1 >= wo+w2
できた！
w0+w2 <= s1を証明したい

'''
