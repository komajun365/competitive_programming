# a,b = map(int,input().split())
# a = list(map(int,input().split()))
# a = [list(map(int,input().split())) for _ in range(n)]

# 検討?分　実装分 バグとり分

import sys
import os
f = open('../../input.txt', 'r')
sys.stdin = f

n,q = map(int,input().split())
ss = [tuple(map(int,input().split())) for _ in range(q)]

# [forllow,follower]
follow = [[set(),set()] for _ in range(n+1)]
for s in ss:
    if(s[0]==1):
        a,b = s[1:]
        follow[a][0].add(b)
        follow[b][1].add(a)
    elif(s[0]==2):
        a = s[1]
        follow[a][0] = follow[a][0]|follow[a][1]
        for x in follow[a][0]:
            follow[x][1].add(a)
    elif(s[0]==3):
        a = s[1]
        tmp = set()
        for x in follow[a][0]:
            tmp = tmp|follow[x][0]
        follow[a][0] = follow[a][0]|tmp
        follow[a][0].discard(a)
        for x in follow[a][0]:
            follow[x][1].add(a)

for i in range(1,n+1):
    ans = ''
    for j in range(1,n+1):
        if(j in follow[i][0]):
            ans += 'Y'
        else:
            ans += 'N'
    print(ans)
