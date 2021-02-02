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

n = int(input())
a = list(map(int,input().split()))

c = 0
for i in range(2,n):
    c = c^a[i]

start = a[0]
a,b = a[0],a[1]
if((a^b)==c):
    print(0)
    exit()

dif = a+b-c
if(dif%2==1):
    print(-1)
    exit()

dif = dif//2
for i in range(40):
    if((c >> i)&1)&((dif >> i)&1):
        print(-1)
        exit()

if(dif > start):
    print(-1)
    exit()

goal = dif

for i in range(40,-1,-1):
    if(c >> i)&1:
        if(goal + 2**i <= start):
            goal += 2**i

if(goal==0):
    print(-1)
    exit()

print(start-goal)





'''
最上位の桁の場所が変わらない限り同じでは？

'''
