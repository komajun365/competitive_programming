import sys
import os
f = open('../../input.txt', 'r')
sys.stdin = f

s = input()

ans = ''
for i in range(len(s)):
    ans = ans + 'x'

print(ans)
