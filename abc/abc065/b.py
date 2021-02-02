# a,b = map(int,input().split())
# a = list(map(int,input().split()))
# a = [list(map(int,input().split())) for _ in range(n)]

import sys
import os
f = open('../../input.txt', 'r')
sys.stdin = f

import sys
input = sys.stdin.readline

n = int(input())
a = []
for _ in range(n):
    a.append(int(input()))

ans = 0
now = 0
for _ in range(n):
    now = a[now] -1 
    ans += 1
    if(now == 1):
        print(ans)
        exit()

print(-1)
