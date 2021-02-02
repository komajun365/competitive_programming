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

ai,ao,at,aj,al,As,az = map(int,input().split())

ans = (ai//2)*4 + ao*2 + (aj//2)*4 + (al//2)*4
if(ai>0)&(aj>0)&(al>0):
    ai -= 1
    aj -= 1
    al -= 1
    tmp = 6 + (ai//2)*4 + ao*2 + (aj//2)*4 + (al//2)*4
    ans = max(ans,tmp)
print(ans//2)
