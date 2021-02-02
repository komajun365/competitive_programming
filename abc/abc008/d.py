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

from functools import lru_cache

w,h = map(int,input().split())
n = int(input())
xy = [list(map(int,input().split())) for _ in range(n)]

if(n==1):
    ans = w+h-1
    print(ans)
    exit()


area = [[-1]*n for _ in range(n)]
for i in range(n-1):
    xi,yi = xy[i]
    for j in range(i+1,n):
        xj,yj = xy[j]
        if(xi<xj)&(yi<yj):
            area[i][j] = 0
            area[j][i] = 2
        elif(xi<xj)&(yi>yj):
            area[i][j] = 3
            area[j][i] = 1
        elif(xi>xj)&(yi<yj):
            area[i][j] = 1
            area[j][i] = 3
        elif(xi>xj)&(yi>yj):
            area[i][j] = 2
            area[j][i] = 0


# cnt = 0
@lru_cache(maxsize=10**8)
def calc(N,S,E,W,rems):
    # global cnt
    # cnt += 1
    res = 0
    for i in rems:
        tmp = (N-S) + (E-W) + 1
        xi,yi = xy[i]
        rems_new = [[] for _ in range(4)]
        for j in rems:
            if(i==j):
                continue
            rems_new[ area[i][j] ].append(j)

        if(rems_new[0]):
            tmp += calc(N,yi+1,E,xi+1,tuple(rems_new[0]))
        if(rems_new[1]):
            tmp += calc(N,yi+1,xi-1,W,tuple(rems_new[1]))
        if(rems_new[2]):
            tmp += calc(yi-1,S,xi-1,W,tuple(rems_new[2]))
        if(rems_new[3]):
            tmp += calc(yi-1,S,E,xi+1,tuple(rems_new[3]))
        res = max(res,tmp)
    return res


ans = calc(h,1,w,1,tuple(range(n)))
print(ans)

# print(cnt)

'''
どれか1個を作動させると、領域は4分割される。
2個目を発動すると、領域が3つ増える。


最後がa->b

状態を決めれば、
そこまでの操作の仕方にかかわらず、
残りの操作による最大獲得個数は固定。

ところが状態は2**30あるのであった。

なんとなくですが、再帰で良い感じに溶けると思いたいです。

'''
