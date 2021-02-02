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
attack = 0
for i in ss:
    if(not i in ks):
        attack += 1

if(attack==0):
    print(len(s))
    exit()

max_hit = unknown*3-2

dp_k = [[0] * (max_hit+1) for _ in range(attack+1)]
#知らないことが確定しているケース
dp_u = [[0] * (max_hit+1) for _ in range(attack+1)]
dp_u[0][0] = 1

for i in range(attack):
    if(i >= 1):
        tot = sum(dp_k[i])
        for j in range(max_hit+1):
            dp_k[i][j] /= tot
    for j in range(max_hit):
        #知ってるけど使ってないkeyの数
        not_used = (j-i)//2
        #知らないkeyの数
        not_known = unknown - i - not_used
        if(not_known==1):
            not_used += 1
            not_known -= 1

        #すでに覚えていたkey
        dp_k[i+1][j+1] += dp_k[i][j] *  (not_used / (not_used + not_known))
        #まだ覚えていなかったkey
        dp_u[i][j] += dp_k[i][j] *  (not_known / (not_used + not_known))

        #知らなかったけどあてずっぽうで突破
        if(not_known>1):
            dp_k[i+1][j+1] += dp_u[i][j] * (1 / (not_known))
            #知らなかったし失敗
            dp_u[i][j+2] += dp_u[i][j] * ((not_known-1) / not_known)
        else:
            dp_k[i+1][j+1] += dp_u[i][j]

ans = len(s) - attack
tot = sum(dp_k[-1])
for j in range(max_hit+1):
    dp_k[-1][j] /= tot
for j in range(max_hit+1):
    ans += dp_k[-1][j] * j

print(ans)


for i in dp_k:
    print(i)
    # print(sum(i))
print('')
for i in dp_u:
    print(i)


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
