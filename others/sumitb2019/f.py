import sys
import os
f = open('../../input.txt', 'r')
sys.stdin = f

t = list(map(int, input().split()))
a = list(map(int, input().split()))
b = list(map(int, input().split()))

cycle = t[0] * (a[0] - b[0]) + t[1] * (a[1] - b[1])

if(cycle == 0):
    print('infinity')
    exit()

after_t1 = t[0] * (a[0] - b[0])

if(cycle * after_t1 > 0):
    print(0)
    exit()

after_t1 = abs(after_t1)
cycle = abs(cycle)

ans = 1 + 2 * (after_t1//cycle) - (after_t1 % cycle == 0) * 1

print(ans)
