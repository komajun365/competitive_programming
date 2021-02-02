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


s = input()
k = input()

ss = set(s)
ks = set(k)

unknown = 36 - len(ks)
will_use = 0
for i in ss:
    if(not i in ks):
        will_use += 1
not_use = unknown - will_use

if(will_use==0):
    print(len(s))
    exit()

max_hit = will_use*3 + not_use*2

dp = [[] for _ in range(will_use+1)]
for i in range(will_use+1):
    dp[i] = [[0] * (max_hit+1) for _ in range(not_use+1)]

dp[will_use][not_use][0] = 1

for i in range(will_use,0,-1):
    for j in range(not_use,-1,-1):
        for k in range(0,max_hit+1):
            #その時使いたいキー
            if(k < max_hit-1):
                dp[i-1][j][k+1] += dp[i][j][k] * (1/(i+j))
            #その時ではないが後々使うキー
            if(k < max_hit-3):
                dp[i-1][j][k+3] += dp[i][j][k] * ((i-1)/(i+j))
            #1回も使わないキー
            if(j != 0)&(k<max_hit-2):
                dp[i][j-1][k+2] += dp[i][j][k] * (j/(i+j))



ans = len(s) - will_use
tmp = 0
for j in range(not_use+1):
    for k in range(max_hit+1):
        ans += dp[0][j][k] * k
        tmp += dp[0][j][k]

print(ans)
# print(tmp)

# for i in dp:
#     print('======')
#     for j in i:
#         print(j)


'''

sのうち、知らないキーの種類数をnとする
また、すでに知っているキーの数を36-mとする。

高橋君は最低n回最大m回のチャレンジをして、
nに含まれるキーの場所を覚えないといけない。

i文字目の知らなかったキーにたどり着いた時、
既にj回チャレンジしていたとする。

・それまでにそのキーを覚えていた場合
チャレンジなしで突破できる。
確率は？
(j > i-1)、つまり無駄になっているチャレンジが1回以上あったとして
(j-i-1) / (m-(i-1))

・それまでに覚えていない場合、確率遷移する。
(i,j)→(i+1,j+1) ：突破できるケース
確率は、1/(m-j)
試行回数は1回

(i,j)→(i,j+1) ：突破できないケース
確率は、(m-j-1)/(m-j)
試行回数は2回

全部の期待を計算していけばよい

'''


'''
結局、知らないキーをどの順番でたたくか、なのかしら。

・その時使いたいキー
+1
・その時ではないが後々使うキー
+3
・1回も使わないキー
+2

dp[使う＆知らないキーの数][使わない＆知らないキーの数][たたいた回数]
dp[i][j][k]

・その時使いたいキー
dp[i-1][j][k+1] += dp[i][j][k] * (1/(i+j))
・その時ではないが後々使うキー
dp[i-1][j][k+3] += dp[i][j][k] * ((i-1)/(i+j))
・1回も使わないキー
dp[i][j-1][k+2] += dp[i][j][k] * (j/(i+j))


'''
