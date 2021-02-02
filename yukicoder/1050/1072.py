# a,b = map(int,input().split())
# a = list(map(int,input().split()))
# a = [list(map(int,input().split())) for _ in range(n)]

# import sys
# read = sys.stdin.buffer.read
# readline = sys.stdin.buffer.readline
# readlines = sys.stdin.buffer.readlines

# 検討?分　実装分 バグとり分

import sys
import os
f = open('../../input.txt', 'r')
sys.stdin = f

import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
from collections import defaultdict

n,x = map(int,readline().split())
a = list(map(int,read().split()))

ans = 0
d = defaultdict(int)
for i in a:
    ans += d[i^x]
    d[i] += 1

print(ans)



'''
10101^00100 = 10001
10101^10001 = 00100
'''
