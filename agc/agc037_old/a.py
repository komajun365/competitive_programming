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

s = input()
ans = 0
i = 0
before = '#'
while(i<len(s)):
    if(s[i]!=before):
        before = s[i]
        i += 1
        ans += 1
    else:
        before = '#'
        i += 2
        ans += 1

if(i!=len(s)):
    ans -= 1

print(ans)
