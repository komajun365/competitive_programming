import sys
import os
f = open('../../input.txt', 'r')
sys.stdin = f

c = input()
print ( chr(ord(c) + 1))
