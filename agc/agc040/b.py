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
cut = [0]
for i in range(len(s)-1):
    if(s[i:i+2] == '><'):
        cut.append(i+1)
cut.append(len(s)+1)

ans = 0
for i in range(len(cut)-1):
    ss = s[cut[i]:cut[i+1]]
    left = ss.count('<')
    right = ss.count('>')
    ans += left*(left+1)//2 + right*(right+1)//2 - min(left,right)

print(ans)
