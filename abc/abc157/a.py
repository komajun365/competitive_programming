import sys
import os
f = open('../../input.txt', 'r')
sys.stdin = f

n = int(input())

print((n+1)//2)
