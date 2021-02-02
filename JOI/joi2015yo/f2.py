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
f = open('../../input.txt', 'r')
sys.stdin = f

from heapq import heappop,heappush

n,d = map(int,input().split())
xy = [tuple(map(int,input().split())) for _ in range(n)]

if(n==1):
    x,y = xy[0]
    if(x<=d):
        print(y)
    else:
        print(0)
    exit()

n2 = min(15,n-1)
n1 = n-n2

xy1 = tuple(xy[:n1])
xy2 = tuple(xy[n1:])

def calc_g(n1,xy1):
    g1 = []
    for i in range(3**n1):
        dx,dy = 0,0
        j = 0
        while(i>0):
            if(i%3==1):
                dx += xy1[j][0]
                dy += xy1[j][1]
            elif(i%3==2):
                dx -= xy1[j][0]
                dy -= xy1[j][1]
            i //= 3
            j += 1
        g1.append((dx,dy))
    return g1

g1 = calc_g(n1,xy1)
g2 = calc_g(n2,xy2)

g1.sort()
g2.sort(reverse=True)

ans = 0
left = 0
right = 0
hq = []
done = []

for x,y in g1:
    # -d-x ~ d-x
    while(right < len(g2)):
        if(g2[right][0] >= -x-d):
            heappush(hq,-1*g2[right][1])
            right += 1
        else:
            break
    while(left < len(g2)):
        if(g2[left][0] > -x+d):
            heappush(done,-1*g2[left][1])
            left += 1
        else:
            break

    while(True):
        if(not hq):
            g2_y = 10**18 * -1
            break

        if(not done):
            g2_y = hq[0]*-1
            break

        if(hq[0] == done[0]):
            heappop(hq)
            heappop(done)
        else:
            g2_y = hq[0]*-1
            break

    ans = max(ans,y+g2_y)

print(ans)


'''

'''
