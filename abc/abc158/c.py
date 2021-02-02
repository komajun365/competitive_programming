import sys
import os
f = open('../../input.txt', 'r')
sys.stdin = f

a,b = map(int, input().split())

for i in range(20000):
    if( a== int(i*0.08)):
        if( b == int(i*0.1)):
            print(i)
            exit()

print(-1)
