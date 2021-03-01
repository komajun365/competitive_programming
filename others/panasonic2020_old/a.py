import sys
import os
f = open('../../input.txt', 'r')
sys.stdin = f

k = int(input())
s = [1, 1, 1, 2, 1, 2, 1, 5, 2, 2, 1, 5, 1, 2, 1, 14, 1, 5, 1, 5, 2, 2, 1, 15, 2, 2, 5, 4, 1, 4, 1, 51]

print(s[k-1])
