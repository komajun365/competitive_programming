# a,b = map(int,input().split())
# a = list(map(int,input().split()))
# a = [list(map(int,input().split())) for _ in range(n)]

import sys
import os
f = open('../../input.txt', 'r')
sys.stdin = f

n = int(input())
s = input()
if(s[:n//2] == s[n//2:])&(n%2==0):
    print('Yes')
else:
    print('No')
