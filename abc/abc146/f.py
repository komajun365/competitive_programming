# a,b = map(int,input().split())
# a = list(map(int,input().split()))
# a = [list(map(int,input().split())) for _ in range(n)]

import sys
import os
f = open('../../input.txt', 'r')
sys.stdin = f

n,m = map(int,input().split())
s = input()

s_0 = []
for i in range(n+1):
    if(s[i] == '0'):
        s_0.append(i)

# 二分木
import bisect

now = n
ans_rev = []
while(now != 0):
    next_i = bisect.bisect_left(s_0, now-m)
    next = s_0[next_i]
    if(now == next):
        print(-1)
        exit()
    ans_rev.append(now-next)
    now = next

print(' '.join(map(str, ans_rev[::-1])))
