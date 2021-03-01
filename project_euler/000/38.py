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

ans = 0
for i in range(1,10000):
    nums = ''
    for j in range(1,10):
        x = i*j
        nums += str(x)
        if len(nums) >= 9:
            break
    if len(nums) != 9:
        continue
    cnt = 0
    for si in '123456789':
        if si in nums:
            cnt += 1
    if cnt == 9:
        ans = max(ans, int(nums))
        print(i,nums)

print(ans)



