# a,b = map(int,input().split())
# a = list(map(int,input().split()))
# a = [list(map(int,input().split())) for _ in range(n)]

import sys
import os
f = open('../../input.txt', 'r')
sys.stdin = f

s = input()
n = len(s)
s_1 = s[::-1]

s_2a = s[:(n-1)//2]
s_2b = s_2a[::-1]

s_3a = s[(n+3)//2 -1  :]
s_3b = s_3a[::-1]

if(s==s_1)&(s_2a==s_2b)&(s_3a==s_3b):
    print('Yes')
else:
    print('No')
