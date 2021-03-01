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

import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
from heapq import heappop,heappush
from copy import deepcopy

n = int(readline())
lr = list(map(int,read().split()))


hq_left = []
hq_right = []

for i in range(n):
    l,r = lr[i*2:i*2+2]
    heappush(hq_left,(-1*l,i))
    heappush(hq_right,(r,i))

hq_left_origin = deepcopy(hq_left)
hq_right_origin = deepcopy(hq_right)

done = [0] * n
ans = -1*10**5
now = 10**5
while(len(hq_left)>0)&(len(hq_right)>0):
    while(hq_left):
        l,ind_l = hq_left[0]
        l *= -1
        if(done[ind_l] == 1):
            heappop(hq_left)
        else:
            break
    else:
        break

    while(hq_right):
        r,ind_r = hq_right[0]
        if(done[ind_r] == 1):
            heappop(hq_right)
        else:
            break
    else:
        break

    if( l-now > now-r):
        if(l > now):
            ans += l-now
            now = l
        done[ind_l] = 1
        heappop(hq_left)
    else:
        if(now > r):
            ans += now-r
            now = r
        done[ind_r] = 1
        heappop(hq_right)

ans += abs(now)

ans2 = -1*10**5
now = -1 * 10**5
hq_left = deepcopy(hq_left_origin)
hq_right = deepcopy(hq_right_origin)
done = [0] * n

while(len(hq_left)>0)&(len(hq_right)>0):
    while(hq_left):
        l,ind_l = hq_left[0]
        l *= -1
        if(done[ind_l] == 1):
            heappop(hq_left)
        else:
            break
    else:
        break

    while(hq_right):
        r,ind_r = hq_right[0]
        if(done[ind_r] == 1):
            heappop(hq_right)
        else:
            break
    else:
        break

    if( l-now > now-r):
        if(l > now):
            ans2 += l-now
            now = l
        done[ind_l] = 1
        heappop(hq_left)
    else:
        if(now > r):
            ans2 += now-r
            now = r
        done[ind_r] = 1
        heappop(hq_right)

ans2 += abs(now)


print(max(ans,ans2))


'''
できるだけふらふらさせたい

0に戻ってくるわけなので、行った分は帰ってくる。

貪欲じゃダメ？なんだよね？

よさそう？とりあえず実装してみる？

ほぼ貪欲でよさそうだけど、
最後に戻ってくる分でずれそう？



'''
