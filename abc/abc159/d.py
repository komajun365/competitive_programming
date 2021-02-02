# a,b = map(int,input().split())
# a = list(map(int,input().split()))
# a = [list(map(int,input().split())) for _ in range(n)]

import sys
import os
f = open('../../input.txt', 'r')
sys.stdin = f

n = int(input())
a = tuple(map(int,input().split()))

c_dic = {}
for i in range(1,n+1):
    c_dic[i] = 0

for i in a:
    c_dic[i] += 1

ans_dic = {}
ans = 0
for i in range(1,n+1):
    ans_dic[i] = (c_dic[i] * (c_dic[i] -1) )//2
    ans += ans_dic[i]

for i in range(n):
    print(ans - max(c_dic[a[i]] -1 , 0))
