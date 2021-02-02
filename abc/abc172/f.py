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

while(a > 1):
    a_next = a - (2**((a-1).bit_length()-1) -1)
    b_next = 2**(b).bit_length() - b

    a -= min(a_next,b_next)
    b += min(a_next,b_next)

    print(a,b)

    if((a^b)==c):
        print(start - a)
        exit()

print(-1)

'''
最上位の桁の場所が変わらない限り同じでは？

'''
