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
ans = 0
for i in range(1,n):
    ans += ((n-1)//i)
print(ans)


# for i in range(1,n):
#     if(i**2 > n):
#         break
#     ans += 1
# ans //= 2
# print(ans)