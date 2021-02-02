import sys
import os
f = open('../../input.txt', 'r')
sys.stdin = f

n,l = map(int,input().split())
amidas = [input() for _ in range(l)]
o_s = input()

l_point = o_s.find('o')

for i in range(l-1, -1, -1):
    amida = amidas[i]
    for j in [-1,1]:
        if((l_point + j < 0) | (l_point + j > 2*n -2) ):
            continue

        if(amida[l_point + j] == '-'):
            l_point += j*2
            break

print(1 + l_point//2)
