# a,b = map(int,input().split())
# a = list(map(int,input().split()))
# a = [list(map(int,input().split())) for _ in range(n)]

# https://www.ioi-jp.org/camp/2007/2007-sp-tasks/2007-sp-day2_21.pdf

import sys
import os
f = open('../../input.txt', 'r')
sys.stdin = f

p = int(input())
n = int(input())

cnt = [0] * p
for i in range(p):
    cnt[pow(i,n,p)] += 1

ans0 = 0
for i in range(p):
    ans0 += cnt[i]*cnt[(-i)%p]*cnt[0]

ans1 = 0
for i in range(p):
    ans1 += cnt[i]*cnt[(1-i)%p]*cnt[1]

mul1 = 0
for i in range(1,p):
    mul1 += (cnt[i] > 0)

ans = ans0 + ans1*mul1
print(ans)
