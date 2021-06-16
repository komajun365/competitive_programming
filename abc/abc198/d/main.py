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
# f = open('../../../input.txt', 'r')
# sys.stdin = f

import itertools
s1 = input()
s2 = input()
s3 = input()

ch = set()
for s in [s1,s2,s3]:
    for si in s:
        ch.add(si)

l = len(ch)
if l > 10:
    print('UNSOLVABLE')
    exit()

d = dict()
for i,si in enumerate(ch):
    d[si] = i

def check(p):
    n1 = 0
    n2 = 0
    n3 = 0
    for si in s1:
        n1 = n1*10 + p[d[si]]
        if n1 == 0:
            return False
    for si in s3:
        n3 = n3*10 + p[d[si]]
        if n3 == 0:
            return False
    for si in s2:
        n2 = n2*10 + p[d[si]]
        if n2 == 0:
            return False
    if n1 + n2 == n3:
        print(n1)
        print(n2)
        print(n3)
        exit()
    return False


for p in itertools.permutations(range(10),l):
    p = list(p)
    res = check(p)

print('UNSOLVABLE')

    