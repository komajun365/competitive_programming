import sys
import os
f = open('../../input.txt', 'r')
sys.stdin = f

n = int(input())

ans_b = []
ans_n = ['a']

s = ['a','b','c','d','e','f','g','h','i','j']

for i in range(1,n):
    ans_b = ans_n.copy()
    ans_n = []
    for j in ans_b:
        plus = 1
        ans_n.append(j+'a')
        while( j.count(s[plus-1]) > 0):
            ans_n.append(j+ s[plus])
            plus += 1

ans = sorted(ans_n)

for i in ans:
    print(i)
