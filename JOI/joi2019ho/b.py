# a,b = map(int,input().split())
# a = list(map(int,input().split()))
# a = [list(map(int,input().split())) for _ in range(n)]

# import sys
# read = sys.stdin.buffer.read
# readline = sys.stdin.buffer.readline
# readlines = sys.stdin.buffer.readlines

# 検討12分　実装8分 バグとり7分

import sys
import os
f = open('../../input.txt', 'r')
sys.stdin = f

import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
# ヒープキュー（最小値・最大値の取得）
from heapq import heappop,heappush,heapify

n,m = map(int,readline().split())
data = list(map(int,read().split()))

hq = []
for i in range(0,n*2,2):
    s,v = data[i:i+2]
    heappush(hq, (-((v<<30) + s),s) )

c = data[2*n:]
c.sort(reverse=True)

ans = 0
for size in c:
    while(hq):
        v,s = heappop(hq)
        if(size >= s):
            ans += 1
            break

print(ans)

'''
最大値を取り出すheapqを使う。
すべての絵をheapqに突っ込んでおく。

大きい額から順番に入れる絵を決める。
heappopした絵が、額に入るサイズなら決定。次の額へ。
額に入らないなら、再度絵を取り出す。

この繰り返しで、額or絵がなくなるまでに展示できる絵の最大数が答え。
O(M+NlogN)でとける。

価値が同じで、大きさが小さい絵を先に使ってしまうと困る。
x = v*(2**30) + s とすればよさそう
'''
