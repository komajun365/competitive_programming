import sys
import os
f = open('../../input.txt', 'r')
sys.stdin = f

n = int(input())
d = list(map(int, input().split()))

d.sort()
a = d[-1 + n//2]
b = d[n//2]
print(b-a)
