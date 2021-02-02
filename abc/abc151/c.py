import sys
import os
f = open('../../input.txt', 'r')
sys.stdin = f

n,m = map(int, input().split())

ac = [0]*n
wa = [0]*n

for i in range(m):
    p, s = input().split()
    p = int(p)

    if(s=='AC'):
        ac[p-1] = 1
    else:
        if(ac[p-1] == 0):
            wa[p-1] += 1

for i in range(n):
    wa[i] = wa[i] * ac[i]

print('{} {}'.format(sum(ac), sum(wa)))
