# a,b = map(int,input().split())
# a = list(map(int,input().split()))
# a = [list(map(int,input().split())) for _ in range(n)]

import sys
import os
f = open('../../input.txt', 'r')
sys.stdin = f

import sys
input = sys.stdin.readline

h,w,n = map(int,input().split())
ab = [tuple(map(int,input().split())) for _ in range(n)]

ans = [0] * 10
ans[0] = (h-2)*(w-2)

black = set(ab)
checked = set()

for tmp in ab:
    a,b = tmp
    y0 = max(1,a-2)
    y1 = min(h,a+2)-1
    x0 = max(1,b-2)
    x1 = min(w,b+2)-1
    for i in range(x0,x1):
        for j in range(y0,y1):
            if ((j,i) in checked):
                continue
            tmp = 0
            for x in range(3):
                for y in range(3):
                    tmp += ((j+y,i+x) in black)
            ans[0] -= 1
            ans[tmp] += 1
            checked.add((j,i))

print('\n'.join(map(str,ans)))
