# a,b = map(int,input().split())
# a = list(map(int,input().split()))
# a = [list(map(int,input().split())) for _ in range(n)]

# https://www.ioi-jp.org/camp/2008/2008-sp-tasks/2008-sp_tr-day2_21.pdf
# 検討6分　実装10分 バグとり8分

import sys
import os
f = open('../../input.txt', 'r')
sys.stdin = f

import sys
input = sys.stdin.readline
from collections import deque

n,m = map(int,input().split())

x = []
y = []
for _ in range(m):
    x_in, y_in = map(int,input().split())
    x.append(x_in)
    y.append(y_in)

x.sort()
y.sort()

ng = -1
ok = 10**9

def calc(d,tester):
    i = 0
    now = -1
    res = 0
    while(i<m):
        if(tester[i] > now):
            now = tester[i] + d
            res += 1
        i += 1
    return res

for _ in range(50):
    mid = (ng+ok)//2
    num = calc(mid,x) + calc(mid,y)
    if(num <= n):
        ok = mid
    else:
        ng = mid

    if(ok-ng==1):
        break

print(ok)

# print(x)
# print(y)

'''
方針
・二分探索
dを固定したときに、
x軸方向とy軸方向で必要な監視装置の数を計算する
を繰り返す

・必要な監視装置の数の計算
ソートしておけばO(M)
ソートにO(MlogM)

全体でO(MlogN)
'''
