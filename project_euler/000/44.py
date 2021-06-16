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
f = open('p042_words.txt', 'r')
sys.stdin = f

n = 15000
inf = n**3

ps = set()
for i in range(1,n+1):
    x = i * (3*i-1) //2
    ps.add(x)

ans = inf
pl = list(ps)
for i in range(n-1):
    x = pl[i]
    for j in range(i+1,n):
        y = pl[j]
        if x+y in ps and y-x in ps:
            ans = min(ans,y-x)
            print(x,y,y-x)

print(ans)
















