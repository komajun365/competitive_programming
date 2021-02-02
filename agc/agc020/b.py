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

k = int(input())
a = list(map(int,input().split()))

upper,lower = 2,2

for ai in a[::-1]:
    lower = (1+(lower-1)//ai)*ai
    upper = (1 + upper//ai)*ai -1
    if(upper < lower):
        print(-1)
        exit()
    # print(lower,upper)

print(' '.join(map(str,[lower,upper])))



'''

Ai,Ajを経てx人になっていたとする。
x = pAj
pAj + q = rAi

普通に後ろから計算できそう。


'''
