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

n,m = map(int,input().split())
a = list(map(int,input().split()))

done = set()
ans = []

for num in a[::-1]:
    if(not num in done):
        ans.append(num)
        done.add(num)

print(' '.join(map(str,ans)))


#
# n,m = map(int,input().split())
# a = list(map(int,input().split()))
#
# team = [0] * (m+1)
# ans = []
#
# for ind,num in enumerate(a[::-1]):
#     if(team[num] == 0):
#         team[num] = n-ind
#         ans.append(num)
#
# print(' '.join(map(str,ans)))
