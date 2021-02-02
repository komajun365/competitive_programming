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

ones = set()
x = 1
while(not x in ones):
    ones.add(x)
    x = (x*10)%k

num = 1
mask = (1<<k) -1
for i in range(1,46):
    next = 0
    for j in ones:
        next |= (num<<j)
    num = (next&mask) | (next>>k)

    if(num%2==1):
        print(i)
        exit()




'''
k = 6

012345

100000
010010

001001
0
000001
0010
001001


[a,b,c]

dp[1] = (1<<a)|(1<<b)|(1<<c)
dp[2] = ()


'''
