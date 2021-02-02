import sys
import os
f = open('../../input.txt', 'r')
sys.stdin = f

n,a,b = map(int, input().split())

cyc = n // (a+b)
ans = cyc * a + min(n%(a+b), a)
print(ans)
