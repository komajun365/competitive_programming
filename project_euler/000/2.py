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

ans = 2
num = [1,2]
for i in range(1000):
    num[i%2]=sum(num)
    if(num[i%2]>4*10**6):
        break
    if(num[i%2]%2==0):
        ans += num[i%2]


print(ans)
print(num)
