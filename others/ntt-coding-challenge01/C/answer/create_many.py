#!/usr/bin/env python

# 13-sample00を作成するスクリプト

from random import randint, shuffle

s = set()
for v in range(3, 100000, 2):
    if len(s) > 997:
        break
    s.add(v)
    while v * v <= 1000000000:
        s.add((v * v - 1) // 2)
        if ((v * v + 1) // 2) in s:
            break
        s.add((v * v + 1) // 2)
        v = (v * v + 1) // 2
print(f'{len(s)} 0')
s = list(map(str, s))
shuffle(s)
print(' '.join(s))