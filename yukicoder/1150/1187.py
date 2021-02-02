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
iter = 1
ok = 0
ng = 1000
while iter <= 24:
    mid = (ok+ng)//2
    print ("? {}".format(mid))
    sys.stdout.flush()
    iter += 1
    res = input()
    if(res == 'safe'):
        ok = mid
        continue

    print ("? {}".format(mid+1))
    sys.stdout.flush()
    iter += 1
    res = input()
    if(res=='safe'):
        ok = mid+1
    else:
        ng = mid

print("! {}".format(ok))
sys.stdout.flush()
