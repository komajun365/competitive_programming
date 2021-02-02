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

a,b,c = map(int,input().split())

inroot = b**2-4*a*c
if(inroot < 0):
    print('imaginary')
elif(inroot==0):
    print(-b/(2*a))
else:
    ans = [0]*2
    ans[0] = (-b+inroot**0.5)/(2*a)
    ans[1] = (-b-inroot**0.5)/(2*a)
    ans.sort()
    print(' '.join(map(str,ans)))
