import sys
import os
f = open('../../input.txt', 'r')
sys.stdin = f

n = int(input())
s = [input() for _ in range(n)]

ans = 0

before_j = n
for i in range(n):
    tmp = s[i][:before_j]
    ind = tmp.rfind('.')
    if(ind == -1):
        before_j = n
    else:
        ans += 1
        before_j = ind

print(ans)
