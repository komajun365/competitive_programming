import sys
import os
f = open('../../input.txt', 'r')
sys.stdin = f

h,a = map(int, input().split())

print( (h-1)//a + 1)
