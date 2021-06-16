# a,b = map(int,input().split())
# a = list(map(int,input().split()))
# a = [list(map(int,input().split())) for _ in range(n)]

import sys
import os
f = open('../../input.txt', 'r')
sys.stdin = f

n = int(input())
t,a = map(int,input().split())

for i in range(n-1):
    ti, ai = map(int,input().split())
    cand = set()
    cand.add( 1 + (t+a-1)//ti+ai )
    cand.add( 1 + (a-1)//ai )
    cand.add( 1 + (t-1)//ti )

    tn,an = 10**18,10**18
    for i in cand:
        tt,at = ti*i, ai*i
        if(t<=tt)&(a<=at):
            tn = min(tn, tt)
            an = min(an, at)
    t,a = tn, an

print(t+a)
