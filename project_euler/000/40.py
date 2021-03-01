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
f = open('p018_triangle.txt', 'r')
sys.stdin = f

nums = ''
for i in range(1,10**6):
    nums += str(i)
    if len(nums) > 10**6:
        break

ans = 1
for i in range(7):
    ans *= int(nums[10**i-1])

print(ans)








