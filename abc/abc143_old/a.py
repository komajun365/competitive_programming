import sys
import os
f = open('C:\\Users\\scare\\Documents\\git\\atcoder\\input.txt', 'r')
sys.stdin = f

###############################################

a,b = map(int, input().split())

ans = max(0, a-2*b)
print(ans)
