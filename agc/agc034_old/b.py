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

s = input() + '?'

ans = 0
n_a = 0
n_bc = 0
i = 0
while(i<len(s)):
    if(s[i:i+2]=='BC'):
        n_bc += 1
        i += 2
        continue
    else:
        ans += n_a * n_bc
        n_bc = 0
        if(s[i]=='A'):
            n_a += 1
        else:
            n_a = 0
        i += 1

print(ans)



'''
A と　BC　を交換する捜査
'''
