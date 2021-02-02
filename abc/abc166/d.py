# a,b = map(int,input().split())
# a = list(map(int,input().split()))
# a = [list(map(int,input().split())) for _ in range(n)]

import sys
import os
f = open('../../input.txt', 'r')
sys.stdin = f

x = int(input())
for a in range(-200,201):
    for b in range(-200,201):
        if(a**5 - b**5 == x):
            print(' '.join(map(str,[a,b])))
            exit()
