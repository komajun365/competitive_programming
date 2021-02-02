# a,b = map(int,input().split())
# a = list(map(int,input().split()))
# a = [list(map(int,input().split())) for _ in range(n)]

# import sys
# read = sys.stdin.buffer.read
# readline = sys.stdin.buffer.readline
# readlines = sys.stdin.buffer.readlines

# 検討7分　実装38分 バグとり分

import sys
import os
f = open('../../input.txt', 'r')
sys.stdin = f

import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

inf = 10**10

n,m,x = map(int, readline().split())
data = list(map(int, read().split()))
t = data[:n]

links = [[] for _ in range(n+1)]
deg = [[] for _ in range(n+1)]
for i,ti in enumerate(t,1):
    if(ti!=1):
        links[i] = [[]]
        deg[i] = [inf]
    else:
        links[i] = [[] for _ in range(x*2+1)]
        deg[i] = [inf] * (x*2+1)


it = iter(data[n:])
for a,b,d in zip(it,it,it):
    ta = t[a-1]
    tb = t[b-1]
    if((ta==0)&(tb==0))|((ta==2)&(tb==2)):
        links[a][0].append((d,b,0))
        links[b][0].append((d,a,0))
    elif((ta==1)&(tb==1)):
        links[a][0].append((d,b,0))
        links[b][0].append((d,a,0))
        for i in range(1,x+1):
            links[a][i].append((d,b, max(0,i-d) ))
            links[b][i].append((d,a, max(0,i-d) ))
            links[a][-i].append((d,b, min(0,-i+d) ))
            links[b][-i].append((d,a, min(0,-i+d) ))
    elif(ta!=tb)&(ta+tb==2):
        if(x<=d):
            links[a][0].append((d,b,0))
            links[b][0].append((d,a,0))
    else:
        # aを快適な部屋にしておく
        if(tb==1):
            ta,tb = tb,ta
            a,b = b,a
        links[b][0].append((d,a, (tb-1)*max(0,x-d)))
        if(tb==0):
            for i in range(-x,min(d,x)+1):
                links[a][i].append((d,b,0))
        else:
            for i in range(max(-d,-x), x+1):
                links[a][i].append((d,b,0))

# dijkstra
import heapq
def dijkstra(links,deg , start):
    deg[start][0] = 0
    hq = []
    for i in links[start][0]:
        heapq.heappush(hq, i)
    while(hq):
        cost,i,i2 = heapq.heappop(hq)
        if( deg[i][i2] != inf):
            continue
        deg[i][i2] = cost
        for tmp in links[i][i2]:
            cost_next, j,j2 = tmp
            if(deg[j][j2] == inf):
                heapq.heappush(hq, (cost+cost_next, j,j2))
    return deg

deg = dijkstra(links,deg , 1)

print(min(deg[-1]))

'''
拡張ダイクストラ？
最後に寒い＆暑い部屋から出て何分経っているか、という情報をノードに持たせる。
実装上はノードを増やすことにする。
増やすのは快適な部屋だけで良く、また、寒い部屋、暑い部屋どちらかからの経過時間だけでよい。
X=５０で、寒い部屋から出て30分、暑い部屋から出て20分、というような状況は起こりえない。
→　寒い部屋出て10分後に熱い部屋には入れてしまっているので。

ノード番号：(部屋番号*(2x+1)+x+時間情報)とする。
0の時どの部屋にも入れる。
暑い部屋に入った瞬間に、時間情報が（部屋番号、X）
寒い部屋に入った瞬間に、時間情報が（部屋番号、-X）とする。
'''
