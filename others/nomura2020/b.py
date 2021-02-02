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

t = input()
ans = ''
for ti in t:
    if(ti=='?'):
        ans = ans + 'D'
    else:
        ans = ans + ti

print(ans)

#
# ans = t.count('D') + t.count('?') + t.count('PD') + t.count('P?')
# print(ans)
