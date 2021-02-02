import sys
import os
f = open('../../input.txt', 'r')
sys.stdin = f

h = int(input())

ans = 0
count = 0

while(True):
    if(h==1):
        ans += 2**(count)
        break

    h = h//2
    ans += 2**(count)
    count += 1

print(ans)
