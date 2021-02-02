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

from collections import defaultdict

a = input()
len_a = len(a)
ans = 1 + len_a*(len_a-1)//2

d = defaultdict(int)
for ai in a:
    d[ai] += 1

for key,val in d.items():
    ans -= val*(val-1)//2

print(ans)


'''
aabcaa

それまでに出てきた同じ文字の数を引けばよいかしら？

55+1-1-1-10

5,2,1,1,2
'''
