# oj t -c "python main.py" -d "./tests/" 

# a,b = map(int,input().split())
# a = list(map(int,input().split()))
# a = [list(map(int,input().split())) for _ in range(n)]

# import sys
# read = sys.stdin.buffer.read
# readline = sys.stdin.buffer.readline
# readlines = sys.stdin.buffer.readlines

# 検討?分　実装分 バグとり分

# import sys
# import os
# f = open('input.txt', 'r')
# sys.stdin = f

import itertools

cand = set()
for c in itertools.product([0,1,2], repeat=4):
    c = list(c)
    c += [1]
    cand.add(tuple(c))

deg2 = [[1,0,1],[2,1,1],[2,2,1]]

for x in deg2:
    for y in itertools.product([0,1,2], repeat=2):
        y = list(y)
        y += [1]
        calc = [0,0,0,0,0]
        for i in range(3):
            for j in range(3):
                calc[i+j] += x[i] * y[j]
                calc[i+j] %= 3
        cand.discard(tuple(calc))

for c in cand:
    # print(c[::-1], end='')
    for x in range(3):
        num = 0
        for i,ci in enumerate(c):
            num += x**i * ci
        if num % 3 == 0:
            break
    else:
        print(c[::-1])

