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
s = [input() for _ in range(n)]

ans = ''
for ch in 'abcdefghijklmnopqrstuvwxyz':
    cnt = 50
    for si in s:
        cnt = min(cnt, si.count(ch))

    for i in range(cnt):
        ans += ch

print(ans)
