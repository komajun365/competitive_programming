# a,b = map(int,input().split())
# a = list(map(int,input().split()))
# a = [list(map(int,input().split())) for _ in range(n)]

# https://www.ioi-jp.org/camp/2008/2008-sp-tasks/2008-sp_tr-day1_20.pdf
# 検討14分　実装20分 バグとり6分

import sys
import os
f = open('../../input.txt', 'r')
sys.stdin = f

from collections import deque

n,w,h = map(int,input().split())
pict =  [tuple(map(int,input().split())) for _ in range(h)]

place = [[w,h,0,0] for _ in range(n+1)] #x0,y0,x1,y1
cnt = [0] * (n+1)

for i in range(w):
    for j in range(h):
        c = pict[j][i]
        if(c==0):
            continue
        place[c][0] = min(place[c][0],i)
        place[c][1] = min(place[c][1],j)
        place[c][2] = max(place[c][2],i)
        place[c][3] = max(place[c][3],j)
        cnt[c] += 1

ans = []
remain = set(range(1,n+1))
#どこからも見えない紙
for i,val in enumerate(cnt[1:],1):
    if(val==0):
        ans.append(i)
        remain.remove(i)

# 上下関係の整理
up = [set() for _ in range(n+1)]
down = [set() for _ in range(n+1)]

for c in remain:
    x0,y0,x1,y1 = place[c]
    for i in range(x0,x1+1):
        for j in range(y0,y1+1):
            c2 = pict[j][i]
            if(c != c2)&(0 != c2):
                up[c].add(c2)
                down[c2].add(c)

#down が0枚のものから処理
d = deque()
for c in remain:
    if(not down[c]):
        d.append(c)

while(d):
    c0 = d.pop()
    ans.append(c0)
    for c1 in up[c0]:
        down[c1].remove(c0)
        if(not down[c1]):
            d.append(c1)

print(' '.join(map(str,ans)))
