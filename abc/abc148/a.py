# a,b = map(int,input().split())
# a = list(map(int,input().split()))
# a = [list(map(int,input().split())) for _ in range(n)]

import sys
import os
f = open('../../input.txt', 'r')
sys.stdin = f

a = input()
b = input()
no = {a,b}
for s in ['1','2','3']:
    if(not s in no):
        print(s)
        
