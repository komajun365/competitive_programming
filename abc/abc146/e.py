# a,b = map(int,input().split())
# a = list(map(int,input().split()))
# a = [list(map(int,input().split())) for _ in range(n)]

import sys
import os
f = open('../../input.txt', 'r')
sys.stdin = f

n,k = map(int,input().split())
a = list(map(lambda x: (int(x)-1)%k ,input().split()))

sum_a = sum(a)%k

left = [0] * (n+1)
right = [0] * (n+1)
for i,num in enumerate(a,1):
    left[i] = (left[i-1] + num)%k
for i,num in enumerate(a[::-1],1):
    right[-i-1] = (right[-i] + num)%k

from collections import defaultdict
right_d = defaultdict(int)
right_d_over = defaultdict(int)
ans = 0
for i in range(n,-1,-1):
    ans += right_d[(sum_a - left[i])%k] - right_d_over[(sum_a - left[i])%k]
    right_d[right[i]] += 1
    if( (n-i+1) >= k ):
        right_d_over[right[i+k-1]] += 1

print(ans)
# print(a)
# print(sum_a)
# print(left)
# print(right)
# print(right_d)
