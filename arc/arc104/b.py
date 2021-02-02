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

n,s = input().split()
n = int(n)

ans = 0
a_t = 0
c_g = 0
cnt = [[0]*(n+1) for _ in range(n+1)]
cnt[0][0] = 1
for si in s:
    if(si=='A'):
        a_t += 1
    elif(si=='T'):
        a_t -= 1
    elif(si=='C'):
        c_g += 1
    else:
        c_g -= 1
    ans += cnt[a_t][c_g]
    cnt[a_t][c_g] += 1

print(ans)
