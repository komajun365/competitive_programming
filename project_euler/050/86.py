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

cnt = 0
n = 3000
for c in range(1,n+1):
    c2 = c**2
    for l in range(2,c*2 + 1):
        l2 = l**2
        l_cand = int((c2+l2)**0.5 + 0.1)
        if(c2+l2 == l_cand**2):
            cnt += (c - abs(l - (c+1))+1)//2


    if(cnt > 10**6):
        print(c)
        break
    # print(c,cnt)

print(cnt)

'''
辺のサイズがa<=b<=cの時
(a+b)**2+c**2 = a**2 + b**2 + c**2 + 2ab
これが一番短い

c = k として、
a+b = lで
(a,b)の候補は(l-k,k),(l-k+1,k-1),...,

2<=l<=2k

M=10000くらいまでの全探索でいけるのでは？

'''
