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

num_4 = 0
num_2 = 0
num_1 = 0
for ai in a:
    if(ai%4==0):
        num_4 += 1
    elif(ai%2==0):
        num_2 += 1
    else:
        num_1 += 1

if(num_4 >= num_1):
    print('Yes')
elif(num_4 + 1 == num_1)&(num_2==0):
    print('Yes')
else:
    print('No')
