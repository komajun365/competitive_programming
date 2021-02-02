import sys
import os
f = open('../../input.txt', 'r')
sys.stdin = f

from sys import setrecursionlimit
setrecursionlimit(10**9)
MOD = 10**9 + 7

n = int(input())

neighbor = {}
for i in range(1,n+1):
    neighbor[i] = []

for i in range(n-1):
    x,y = map(int, input().split())
    neighbor[x].append(y)
    neighbor[y].append(x)

def calc(next, base):
    edges = neighbor[next]

    white, black = 1, 1
    for edge in edges:
        if(edge != base):
            white_e, black_e = calc(edge, next)
            white = white *  (white_e + black_e) % MOD
            black = black * white_e % MOD
    return white, black

white, black = calc(1,0)
print((white + black) % MOD )
