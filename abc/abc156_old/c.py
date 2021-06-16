import sys
import os
f = open('../../input.txt', 'r')
sys.stdin = f

n = int(input())
x = list(map(int, input().split()))

ans = 10**10

for j in range(1,101):
    tmp = 0
    for i in range(n):
        tmp += (j - x[i])**2
    ans = min(ans, tmp)

print(ans)
