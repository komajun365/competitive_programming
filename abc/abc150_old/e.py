import sys
import os
f = open('../../input.txt', 'r')
sys.stdin = f

div = (10**9) + 7

n = int(input())
c = list(map(int, input().split()))

c = sorted(c, reverse=True)

ans = 0

exp4_div = [0]*n
exp4_div[0] = 1
for i in range(1,n):
    exp4_div[i] = (exp4_div[i-1]*4)%div

for i in range(n):
    ans = (ans*4 + c[i] * (i+2) * exp4_div[i] ) % div

print(ans)
