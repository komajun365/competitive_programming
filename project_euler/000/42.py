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
f = open('p042_words.txt', 'r')
sys.stdin = f

s = [ x.strip('"') for x in input().split(',')]
longest = 0
for si in s:
    longest = max(longest, len(si))
print(longest)

tris = set()
for i in range(1,longest * 26):
    x = i * (i+1) //2
    if x > longest*26:
        break
    tris.add(x)

ans = 0
for si in s:
    x = 0
    for ch in si:
        x += ord(ch) - ord('A') + 1
    
    if x in tris:
        ans += 1
    # print(si,x)

print(ans)















