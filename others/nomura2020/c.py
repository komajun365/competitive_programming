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

n = int(input())
a = list(map(int,input().split()))

if(a[0]==1):
    if(n==0):
        print(1)
    else:
        print(-1)
    exit()

max_e = sum(a)
if(max_e > 2**n):
    print(-1)
    exit()

not_leaf = [0] * (n+1)
not_leaf[0] = 1

for i,leaf in enumerate(a):
    if(i==0):
        continue

    not_leaf[i] = min(not_leaf[i-1]*2, max_e) - leaf
    if(not_leaf[i] < 0):
        print(-1)
        exit()
    max_e -= leaf

ans = sum(a) + sum(not_leaf)
print(ans)

#
# before = 0
# for i in range(n,-1,-1):
#     num = a[i]
#     if(2**i > num + (before+1)//2):
#
