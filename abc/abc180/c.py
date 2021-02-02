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
ans1 = []
ans2 = []
for i in range(1,10**6+100):
    if(i**2 > n):
        break
    elif(i**2==n):
        ans1.append(i)
        break
    if(n % i == 0):
        ans1.append(i)
        ans2.append(n//i)

ans1 += ans2[::-1]
print('\n'.join(map(str,ans1)))

