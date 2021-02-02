import sys
import os
f = open('../../input.txt', 'r')
sys.stdin = f

n, k, s = map(int, input().split())

dummy = s + 1
if(s == 10**9):
    dummy = 10**9 -1

ans_list = [s] * k
for i in range(k,n):
    ans_list.append(dummy)

print(' '.join(map(str, ans_list)))
