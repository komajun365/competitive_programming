# a,b = map(int,input().split())
# a = list(map(int,input().split()))
# a = [list(map(int,input().split())) for _ in range(n)]

import sys
import os
f = open('../../input.txt', 'r')
sys.stdin = f

s = input()
if(s[2]==s[3])&(s[4]==s[5]):
    print('Yes')
else:
    print('No')
