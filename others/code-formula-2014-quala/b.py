# a,b = map(int,input().split())
# a = list(map(int,input().split()))
# a = [list(map(int,input().split())) for _ in range(n)]

# import sys
# read = sys.stdin.buffer.read
# readline = sys.stdin.buffer.readline
# readlines = sys.stdin.buffer.readlines

# 検討?分　実装分 バグとり分

import sys
import os
f = open('../../input.txt', 'r')
sys.stdin = f

a,b = map(int,input().split())
p = list(map(int,input().split()))
if(b > 0):
    q = list(map(int,input().split()))
else:
    q = []

ans = ['x'] * 10
for i in p:
    ans[i] = '.'
for i in q:
    ans[i] = 'o'

ans = ans[1:] + ans[0:1]

print(' '.join(ans[6:10]))
print(' ' + ' '.join(ans[3:6]))
print('  ' + ' '.join(ans[1:3]))
print('   ' + ans[0])

'''
o x x o
 x . x
  x .
   .

'''
