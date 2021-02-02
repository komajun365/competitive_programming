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
t = input()
len_s = len(s)
len_t = len(t)

ans = len_t
for i in range(len_s-len_t+1):
    tmp = 0
    for j in range(len_t):
        if(s[i+j] != t[j]):
            tmp += 1
    ans = min(ans,tmp)
print(ans)
