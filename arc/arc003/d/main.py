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

import time
start = time.time()

import sys
read = sys.stdin.buffer.read
from random import randint

n,m,k,*ab = map(int,read().split())
bad = 0
tot = 0
while( time.time() - start < 9.5):
    for _ in range(100):
        l = list(range(n))
        for ki in range(k):
            i = randint(0,n-1)
            j = (randint(1,n-1) + i) % n
            l[i],l[j] = l[j],l[i]
        it = iter(ab)
        for a,b in zip(it,it):
            dif = abs(l[a] - l[b])
            if dif == 1 or dif == n-1:
                bad += 1
                break
        
    tot += 100

print(1 - bad/tot)
# print(bad,tot)