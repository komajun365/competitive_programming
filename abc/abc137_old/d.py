# a,b = map(int,input().split())
# a = list(map(int,input().split()))
# a = [list(map(int,input().split())) for _ in range(n)]

import sys
import os
f = open('../../input.txt', 'r')
sys.stdin = f

n,m = map(int,input().split())
db = []

for i in range(n):
    a,b = map(int,input().split())
    if(a<=m):
        db.append([m-a,-1*b])

db.sort(reverse=True)

# ヒープキュー（最小値・最大値の取得）
import heapq
a=[]
heapq.heapify(a)

ans = 0
pnt = 0
day = m-1
while(day>=0):
    if(pnt < len(db)):
        while(db[pnt][0] == day):
            heapq.heappush(a,db[pnt][1])
            pnt += 1
            if(pnt == len(db)):
                break
    day -= 1

    if(len(a) > 0):
        ans -= heapq.heappop(a)

print(ans)
