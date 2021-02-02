# a,b = map(int,input().split())
# a = list(map(int,input().split()))
# a = [list(map(int,input().split())) for _ in range(n)]

# https://www.ioi-jp.org/camp/2008/2008-sp-tasks/2008-sp_tr-day1_20.pdf
# 検討30分　実装8分 バグとり3分 でTLE

import sys
import os
f = open('../../input.txt', 'r')
sys.stdin = f


from collections import deque

m,k = map(int,input().split())

d = deque()
ac,ap = 0,1
bc,bp = 1,1
d.append((1,0))

cnt = 0
cnt1 = 0
while(cnt<k):
    cnt1 += 1
    cc,cp = ac+bc, ap+bp
    if(cp <= m):
        d.appendleft((bc,bp))
        bc,bp = cc,cp
    else:
        cnt += 1
        ac,ap = bc,bp
        bc,bp = d.popleft()
        if(ac >= ap):
            print(-1)
            exit()

print('{} {}'.format(ac,ap))
print(cnt1)

'''
方針
ファレイ数列の性質を使って解く
0/1 と　1/1 からスタートして
小さいほうからk個洗い出すまで間の既約分数を作っていく

dequeで管理

a,bから既約分数cを作る
・cの分母がM以下の場合
→　bをdequeにappendleftして、
　　aとcで次の作業
・cの分母がMより大きい場合
→　aの次に小さい既約分数がbに確定
　 a=b,b=deque.popleft()として次の作業へ

分母がMより大きい分数をK個
分母がMより小さい分数をK＋α個　作るので　ほぼO(K)
※αはそこまで大きくない
'''
