import sys
import os
f = open('../../input.txt', 'r')
sys.stdin = f

s = input()
ans = s.count('A') % 3
if(ans==0):
    print('No')
else:
    print('Yes')
