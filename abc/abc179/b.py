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
cnt = 0
for _ in range(n):
    a,b = map(int,input().split())
    if(a==b):
        cnt += 1
    else:
        cnt = 0
    if(cnt==3):
        print('Yes')
        exit()
print('No')
