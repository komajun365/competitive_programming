import sys
import os
f = open('../../input.txt', 'r')
sys.stdin = f

n, k = map(int,input().split())
p = list(map(int, input().split()))


ans = 0
now = 0
sum = 0
E = [0] * n

for i in range(n):
    E[i] = 0.5 + p[i]/2
    now += E[i]
    if(i == k-1):
        ans = now
    elif(i >= k):
        now -= E[i-k]
        ans = max(ans,now)

print(ans)
