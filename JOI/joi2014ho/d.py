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
from heapq import heappop,heappush

n,m,x = map(int,readline().split())
data = list(map(int,read().split()))
h = [0] + data[:n]

links = [[] for _ in range(n+1)]
for i in range(n,n+3*m,3):
    a,b,t = data[i:i+3]
    if(h[a] >= t):
        links[a].append((t,b))
    if(h[b] >= t):
        links[b].append((t,a))

time = [[-1,-1] for _ in range(n+1)] # time,height
hq = []
heappush(hq,(0,x,1))
while(hq):
    it,ih,i = heappop(hq)
    if(i==n):
        print( it + h[n] - ih )
        exit()
    if(time[i][0] != -1):
        continue
    time[i] = [it,ih]
    for jt,j in links[i]:
        if(time[j][0] != -1):
            continue

        jh = min(h[j], ih-jt)
        heappush(hq, (it+(ih-jh), jh, j))

print(-1)





'''
むずい
拡張ダイクストラだとは思う。
基本はすぐ飛ぶ。
木の頂上を超えた場合は頂上まで下りる。
地面にめり込むのも許す。

Nの木に付いたら、頂上に進むエッジを張る。
いけるかな？

→　最速でたどり着いたとき、一番効率の良い到着方法になっている。（なぜ？）
　なので、高さを覚えておきつつ普通にダイクストラでOK
'''
