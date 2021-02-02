# a,b = map(int,input().split())
# a = list(map(int,input().split()))
# a = [list(map(int,input().split())) for _ in range(n)]

import sys
import os
f = open('../../input.txt', 'r')
sys.stdin = f

n = int(input())
s = input()

ans = ''
for i in s:
    ans += chr((ord(i) + n - ord('A'))%26 + ord('A'))

print(ans)
