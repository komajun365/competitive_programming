import sys
import os
f = open('../../input.txt', 'r')
sys.stdin = f

n,w,k,v = 1000,8,6,8
n,w,k,v = map(int, input().split())
cv = [list(map,input().split()) for _ in range(n)]

stacks = []
for i in range(n//w):
    stacks.append([[0,0] for _ in range(w)])
