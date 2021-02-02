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

e = list(map(int,input().split()))
b = int(input())
l = list(map(int,input().split()))

cnt = 0
for li in l:
    cnt += (li in e)

cnt += (cnt==6)
if(cnt == 5) & (b in l):
    cnt += 1

if(cnt >= 3):
    print(8-cnt)
else:
    print(0)
