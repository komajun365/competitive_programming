# a,b = map(int,input().split())
# a = list(map(int,input().split()))
# a = [list(map(int,input().split())) for _ in range(n)]

# 検討?分　実装分 バグとり分

import sys
import os
f = open('../../input.txt', 'r')
sys.stdin = f

a,b,c,k = map(int,input().split())
if(a >= k):
    print(k)
elif(a+b >= k):
    print(a)
else:
    print(a - (k-a-b))