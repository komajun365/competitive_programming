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

import sys
read = sys.stdin.buffer.read

t,*data = map(int,read().split())

ans = [''] * t
idx = 0
for i in range(t):
    n = data[idx]
    idx += 1
    k,r,c = 0,n,n
    for j in range(0,n**2,n+1):
        k += data[idx+j]
    for j in range(n):
        nums = set()
        for l in range(n):
            num = data[idx + j*n + l]
            if num in nums:
                break
            nums.add(num)
        else:
            r -= 1
    for j in range(n):
        nums = set()
        for l in range(n):
            num = data[idx + l*n + j]
            if num in nums:
                break
            nums.add(num)
        else:
            c -= 1
    ans[i] = 'Case #{}: {} {} {}'.format(i+1,k,r,c)
    idx += n**2

print('\n'.join(ans))
