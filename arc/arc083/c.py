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

import bisect

a,b,c,d,e,f = map(int,input().split())

dp_w = [0] * 31
dp_w[0] = 1
for w in [a,b]:
    for i in range(w,31):
        dp_w[i] |= dp_w[i-w]

water = []
for i in range(1,31):
    if(dp_w[i]==1):
        water.append(i*100)

dp_s = [0] * 1600
dp_s[0] = 1
for w in [c,d]:
    for i in range(w,1600):
        dp_s[i] |= dp_s[i-w]

sugar = []
for i in range(1600):
    if(dp_s[i]==1):
        sugar.append(i)

ans_w =water[0]
ans_s = 0

for wi in water:
    if(f < wi):
        continue
    max_s = min(wi//100 * e, f-wi)
    ind = bisect.bisect_right(sugar,max_s)
    if(ind==0):
        continue
    si = sugar[ind-1]

    if( (ans_w + ans_s) * si > (wi+si) * ans_s):
        ans_w = wi
        ans_s = si

print('{} {}'.format(ans_w+ans_s,ans_s))
