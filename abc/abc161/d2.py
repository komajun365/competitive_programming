# a,b = map(int,input().split())
# a = list(map(int,input().split()))
# a = [list(map(int,input().split())) for _ in range(n)]

import sys
import os
f = open('../../input.txt', 'r')
sys.stdin = f

k = int(input())

# キュー
from collections import deque

d = deque()
for i in range(1,10):
    d.append(i)

for i in range(k):
    tmp = d.popleft()
    right = tmp%10
    if(right!=0):
        d.append(tmp*10+right-1)
    d.append(tmp*10+right)
    if(right!=9):
        d.append(tmp*10+right+1)

print(tmp)
