import sys
import os
f = open('../../input.txt', 'r')
sys.stdin = f

n = int(input())
s = input()

ans = 0
for i in range(n-2):
    temp = s[i:i+3]
    if(temp == 'ABC'):
        ans += 1

print(ans)
