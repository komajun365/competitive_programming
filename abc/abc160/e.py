# a,b = map(int,input().split())
# a = list(map(int,input().split()))
# a = [list(map(int,input().split())) for _ in range(n)]

import sys
import os
f = open('../../input.txt', 'r')
sys.stdin = f

x,y,a,b,c = map(int,input().split())
p = list(map(int,input().split()))
q = list(map(int,input().split()))
r = list(map(int,input().split()))

all = []
for i,val in enumerate([p,q,r]):
    for j in val:
        all.append([j,i])

all.sort(reverse=True)

cnt = [0]*3
ans = 0
for tmp in all:
    i,j = tmp
    if(cnt[0]==x)&(j==0):
        continue
    if(cnt[1]==y)&(j==1):
        continue

    ans += i
    cnt[j] += 1

    if(sum(cnt) == x+y):
        break

print(ans)
