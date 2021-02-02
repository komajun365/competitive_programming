# a,b = map(int,input().split())
# a = list(map(int,input().split()))
# a = [list(map(int,input().split())) for _ in range(n)]

import sys
import os
f = open('../../input.txt', 'r')
sys.stdin = f

n,k,c = map(int,input().split())
s = input()

left = []
cnt = 0
now = 0
while(cnt < k):
    if(s[now]=='o'):
        left.append(now)
        cnt += 1
        now += c
    now += 1

right = []
cnt = 0
now = len(s)-1
while(cnt < k):
    if(s[now]=='o'):
        right.append(now)
        cnt += 1
        now -= c
    now -= 1

right = right[::-1]
for l,r in zip(left,right):
    if(l==r):
        print(l+1)
