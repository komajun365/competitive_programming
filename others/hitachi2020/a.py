import sys
import os
f = open('../../input.txt', 'r')
sys.stdin = f

s = input()
count_ = s.count('hi')
if(count_ * 2 == len(s)):
    print('Yes')
else:
    print('No')
