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

h,w,k = map(int,input().split())
c = [input() for _ in range(h)]

ans = 0
for i in range(2**h):
    for j in range(2**w):
        cnt = 0
        for ii in range(h):
            if((i >> ii)& 1):
                for jj in range(w):
                    if((j >> jj)& 1):
                        cnt += (c[ii][jj]=='#')
        ans += (cnt==k)

print(ans)


'''
36 * 2**6 * 2**6(=64)
'''
