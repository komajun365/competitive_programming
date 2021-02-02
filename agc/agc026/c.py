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

n = int(input())
s = input()

d = defaultdict(int)

s1 = s[:n]
s2 = s[n:][::-1]

for i in range(2**n):
    left,right = [],[]
    for j in range(n):
        if(i >> j)&1:
            left.append(s1[j])
        else:
            right.append(s1[j])
    d[ ''.join(left) + '_' + ''.join(right) ] += 1

ans = 0
for i in range(2**n):
    left,right = [],[]
    for j in range(n):
        if(i >> j)&1:
            left.append(s2[j])
        else:
            right.append(s2[j])
    ans += d[ ''.join(left) + '_' + ''.join(right) ]

print(ans)

'''
cabaacba
abcaabac

半分全列挙？

前半からk個/n-k個選ぶ

後半からn-k個/k個選ぶ

'''
