import sys
import os
f = open('../../input.txt', 'r')
sys.stdin = f

n,p = map(int, input().split())
s = input()

if(p==2)|(p==5):
    ans = 0
    for i in range(n):
        tmp = int(s[i])
        if(tmp%p == 0):
            ans += (i+1)

    print(ans)
    exit()

ans = 0
tmp = 0
rem = [0] * p
rem[0] = 1
for i in range(n):
    tmp = (tmp + int(s[-1 * (i+1)]) * pow(10, i, p)) % p
    ans += rem[tmp]
    rem[tmp] += 1

print(ans)
