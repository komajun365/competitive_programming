# a,b = map(int,input().split())
# a = list(map(int,input().split()))
# a = [list(map(int,input().split())) for _ in range(n)]

import sys
import os
f = open('../../input.txt', 'r')
sys.stdin = f

x = int(input())

n500 = x//500
n5 = (x%500)//5
print(n500*1000 + n5*5)
