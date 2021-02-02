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

import sys
read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
from heapq import heappop,heappush

n = int(readline())
data = readlines()

ans = []
x = 10000
present = set()
seat = [-1] * 21
dh = dict()
for i,s in enumerate(data):
    s = s.split()
    if(s[0] == '0'):
        ni = int(s[1])
        present.add(i)
        seat[ni] = i
        for si in s[3:]:
            if(not si in dh):
                dh[si] = []
            heappush(dh[si], ni*x+i)
    elif(s[0]== '1'):
        bi = s[1]
        if(not bi in dh):
            dh[bi] = []
        while(dh[bi]):
            num = heappop(dh[bi])
            nj = num//x
            j = num%x
            if(j in present):
                ans.append(nj)
                break
        else:
            ans.append(-1)

    else:
        ci = int(s[1])
        present.remove(seat[ci])

print('\n'.join(map(str,ans)))
