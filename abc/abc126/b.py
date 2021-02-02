import sys
import os
f = open('../../input.txt', 'r')
sys.stdin = f

s = input()

s1 = int(s[0:2])
s2 = int(s[2:4])

check1 = ((s1 <= 12) & (s1 != 0))
check2 = ((s2 <= 12) & (s2 != 0))

if(check1):
    if(check2):
        print('AMBIGUOUS')
    else:
        print('MMYY')
else:
    if(check2):
        print('YYMM')
    else:
        print('NA')
