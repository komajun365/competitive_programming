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

n,c = map(int,input().split())
h = list(map(int,input().split()))

ans = (h[-1]-h[0])**2

hq = []
hq_done = []
dif = [0]
dif += [i-j for i,j in zip(h[1:],h[:-1])]
left = list(range(-1,n))
right = list(range(1,n+2))

for i in range(1,n-1):
    di,dj = dif[i:i+2]
    cost = 2*di*dj
    heappush(hq,(cost,i))

now = c*(n-1)
for d in dif:
    now += d**2
ans = now

def hq_pop():
    while(hq_done):
        if(hq_done[0] == hq[0]):
            heappop(hq)
            heappop(hq_done)
        else:
            break

    return heappop(hq)

# print('')
# print(-1, now,ans)
# print(hq)
# print(hq_done)
# print(dif)
# print(left)
# print(right)

for _ in range(n-2):
    cost,l = hq_pop()
    now += cost - c
    ans = min(ans,now)

    r = right[l]
    ll = left[l]
    rr = right[r]
    d_new = dif[l] + dif[r]
    if(ll > 0):
        heappush(hq_done, (2*dif[ll]*dif[l],ll))
        heappush(hq,(2*dif[ll]*d_new,ll))
    if(rr < n):
        heappush(hq_done, (2*dif[r]*dif[rr],r))
        heappush(hq,(2*dif[rr]*d_new,l))

    dif[l] = d_new
    dif[r] = 0
    right[l] = rr
    left[rr] = l

    # print('')
    # print(_, now,ans)
    # print(hq)
    # print(hq_done)
    # print(dif)
    # print(left)
    # print(right)

print(ans)




'''

ジャンプの回数をx回とする。
支払うコストは
(ha-h1)**2 + (hb-ha)**2 + ... + (hn - hm)**2 + c*x

C=0なら
x回ジャンプしたときよりも、X+1回ジャンプしたときのほうがコストは少ない。

ジャンプの回数を1回減らすと、
コストがC減るのにくわえ、
どこかで(hi+hj)**2 -hi**2 - hj**2 増える
(hi+hj)**2 -hi**2 - hj**2 = 2*hi*hj

貪欲でOK？


'''
