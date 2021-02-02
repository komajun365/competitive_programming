# a,b = map(int,input().split())
# a = list(map(int,input().split()))
# a = [list(map(int,input().split())) for _ in range(n)]

import sys
import os
f = open('../../input.txt', 'r')
sys.stdin = f

n,k = map(int,input().split())
ans = set()
for i in range(k):
    d = input()
    a = set(map(int,input().split()))
    ans = ans|a

print(n - len(ans))
