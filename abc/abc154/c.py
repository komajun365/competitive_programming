import sys
import os
f = open('../../input.txt', 'r')
sys.stdin = f

n = int(input())
a = list(map(int, input().split()))

set_a = list(set(a))

if( len(a) == len(set_a)):
    print('YES')
else:
    print('NO')
