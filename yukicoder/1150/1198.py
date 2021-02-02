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
if(n%4==2):
    print(-1)
elif(n in [1,4]):
    print(-1)

else:
    print(1)

'''
a**2-b**2 = n
(a+b)*(a-b)=n

奇数ならある
2



'''
