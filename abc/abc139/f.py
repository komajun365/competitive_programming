# a,b = map(int,input().split())
# a = list(map(int,input().split()))
# a = [list(map(int,input().split())) for _ in range(n)]

# 検討?分　実装分 バグとり分

import sys
import os
f = open('../../input.txt', 'r')
sys.stdin = f

import math

n = int(input())
xy = [list(map(int,input().split())) for _ in range(n)]

#x,yどちらも0のエンジンは捨てる
xy2 = []
for x,y in xy:
    if(x==y==0):
        continue
    xy2.append((x,y))

#使えるエンジンが0個だったら0を出力して終了
n = len(xy2)
if(n==0):
    print(0)
    exit()

degs = [0]
for x,y in xy2:
    deg = math.atan2(y,x)
    deg1 = (deg + math.pi*0.5)%(2*math.pi)
    deg2 = (deg + math.pi*1.5)%(2*math.pi)
    degs.append(deg1)
    degs.append(deg2)

degs.append(2*math.pi)
degs.sort()

ans = 0
for i in range( len(degs)-1 ):
    deg = (degs[i+1]+degs[i])/2
    sum_x = 0
    sum_y = 0
    for x,y in xy2:
        tmp = x*math.cos(deg) + y*math.sin(deg)
        if (tmp > 0):
            sum_x += x
            sum_y += y
    ans = max(ans, (sum_x**2 + sum_y**2)**0.5)

print(ans)

'''
方針
角度θ（0<=θ<2π）を決めて、
その角度への進む距離を最大化することを考える。
各エンジンで進める距離は、
Xi・cosθ＋Yi・sinθで求められる。
Xi・cosθ＋Yi・sinθが0以上ならそのエンジンを採用し、
そうでないならエンジンを採用しないことで、
角度θ方向への距離最大化を行える。

一つのエンジンの採用可否に着目すると、
θと（Xi,Yi）ベクトルの角度差が90度以内なら採用すべきだし、
そうでないなら採用しないことになる。
ひとつのエンジンで360度をちょうど2分割。
N個エンジンがあるということは、
うまく２N個の領域に分ければ、その領域内で採用するエンジンの種類は変わらないようにできる。
なので、２N個の領域でそれぞれ採用すべきエンジンの種類を求め、
それぞれの移動距離の最大値を求めればよい。

２N個の領域の角度を求める：O(N)
※実際には採用エンジンが変わる角度を求めて、
　その後で隣り合う二つの角度の平均を使う。
一つの領域内での移動距離計算：O(N）
全体の計算量：O(N**2)

エンジンで採用可否が変わる角度の求め方
（Xi,Yi）ベクトルの角度→arctan（Yi/Xi）
→　XiかYiが０の時注意。
　 Xiのみ０→Yiプラスならθ＝π/2、Yiマイナスならθ＝3π/2
　 Yiのみ０→Xiプラスならθ＝0、Xiマイナスならθ＝π
　　両方0→使わない

採用可否が変わる角度は、
arctan（Yi/Xi）＋π/2
arctan（Yi/Xi）＋3π/2
（0<=θ<2πにおさまるようにしておく）

'''
