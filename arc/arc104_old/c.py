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

n,*ab = map(int,read().split())

rec = [[-1,-1,-1] for _ in range(2*n)]
it = iter(ab)
for a,b,i in zip(it,it, range(n)):
    a -= 1
    b -= 1
    if(a==-2)&(b==-2):
        continue
    elif(a==-2):
        if(rec[b][0] != -1):
            print('No')
            exit()
        rec[b][0] = i
        rec[b][1] = 1
    elif(b==-2):
        if(rec[a][0] != -1):
            print('No')
            exit()
        rec[a][0] = i
        rec[a][1] = 0
    else:
        if(rec[a][0] != -1)|(rec[b][0] != -1):
            print('No')
            exit()
        rec[a][0] = i
        rec[a][1] = 0
        rec[a][2] = b
        rec[b][0] = i
        rec[b][1] = 1
        rec[b][2] = a

dp = [0] * (n+1)
dp[0] = 1
for i in range(1,n+1):
    for j in range(1,i+1):
        if(dp[i-j] == 0):
            continue
        for k in range((i-j)*2, i*2-j):
            if(rec[k][0]==-1)&(rec[k+j][0]==-1):
                continue
            if(rec[k+j][0]==-1)&(rec[k][1]==0)&(rec[k][2]==-1):
                continue
            if(rec[k][0]==-1)&(rec[k+j][1]==1)&(rec[k+j][2]==-1):
                continue
            if(rec[k][0]==rec[k+j][0])&(rec[k][1]==0)&(rec[k+j][1]==1):
                continue
            break
        else:
            dp[i] = 1

if(dp[-1]==1):
    print('Yes')
else:
    print('No')

print(dp)
print(rec)

'''

dpだとして

dp[x]:=2x階までぴったり埋まる
ができるかどうか判断するには

i＜xについて、
dp[i]==1　かつ
2i+1 ~ 2x について矛盾なく割り当て可能
ならOK

矛盾なく割り当て、を愚直に全確認すればよい？


'''
