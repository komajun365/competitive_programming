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

import itertools
import sys
read = sys.stdin.buffer.read

w,h,n,*xy = map(int,read().split())
Xs = []
Ys = []
it = iter(xy)
for x,y in zip(it,it):
    Xs.append(x)
    Xs.append(x)
    Ys.append(y)
    Ys.append(y)

Xs.sort()
Ys.sort()

cs_x = list(itertools.accumulate(Xs))
cs_y = list(itertools.accumulate(Ys))

def calc(x,y):
    res = [0,0,0] #d,x,y
    if Xs[n] <= x:
        res[1] = Xs[n-1]
        res[0] += cs_x[-1] - cs_x[n-1] - x - (n-1) * res[1]
        res[0] += n * res[1] - cs_x[n-1]
    else:
        res[1] = Xs[n]
        res[0] += cs_x[-1] - cs_x[n-1] - n * res[1]
        res[0] += (n-1) * res[1] - (cs_x[n-1] - x)
    
    if Ys[n] <= y:
        res[2] = Ys[n-1]
        res[0] += cs_y[-1] - cs_y[n-1] - y - (n-1) * res[2]
        res[0] += n * res[2] - cs_y[n-1]
    else:
        res[2] = Ys[n]
        res[0] += cs_y[-1] - cs_y[n-1] - n * res[2]
        res[0] += (n-1) * res[2] - (cs_y[n-1] - y)
    
    return res

ans = [cs_x[-1] + cs_y[-1],0,0]
it = iter(xy)
for x,y in zip(it,it):
    res = calc(x,y)
    if ans[0] > res[0]:
        ans = res
    elif ans[0] == res[0] and ans[1] > res[1]:
        ans = res
    elif ans[0] == res[0] and ans[1] == res[1] and ans[2] > res[2]:
        ans = res

print(ans[0])
print(*ans[1:])

# print(calc(1,1))
# print(calc(3,4))
# print(calc(5,3))






'''
最後の家から交差点まで戻るなら多数決で決まる。
最後の家を決め打ちして計算していけばよい。

O(NlogN)ぐらいでいけそう
'''