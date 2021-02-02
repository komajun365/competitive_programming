import sys
import os
f = open('../../input.txt', 'r')
sys.stdin = f

h = int(input())
w = int(input())
n = int(input())

print( ((n-1) // max(h,w)) + 1)
