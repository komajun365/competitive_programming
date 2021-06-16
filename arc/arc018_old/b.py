# a,b = map(int,input().split())
# a = list(map(int,input().split()))
# a = [list(map(int,input().split())) for _ in range(n)]

import sys
import os
f = open('../../input.txt', 'r')
sys.stdin = f

n = int(input())
xy = [tuple(map(int,input().split())) for _ in range(n)]

ans = 0
for i in range(n-2):
    for j in range(i+1,n-1):
        for k in range(j+1,n):
            x1,y1 = xy[i]
            x2,y2 = xy[j]
            x3,y3 = xy[k]
            s = abs((x2-x1)*(y3-y1) - (x3-x1)*(y2-y1))
            if(s!=0)&(s - (s//2)*2 == 0):
                ans += 1

print(ans)
