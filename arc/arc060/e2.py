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
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
import bisect

n = int(readline())
x = list(map(int,readline().split()))
l = int(readline())
q = int(readline())
ab = list(map(int,read().split()))

dbl = [[] for _ in range(n)]
j = 0
for i in range(n):
    while(j < n-1):
        if(abs(x[j+1] - x[i]) > l):
            break
        j += 1
    dbl[i].append(j)

for i in range(30):
    if(dbl[0][-1] == n-1):
        break
    for j in range(n):
        dbl[j].append(dbl[ dbl[j][i] ][i])

def calc(a,b):
    if(dbl[a][0] >= b):
        return 1
    ind = bisect.bisect_left(dbl[a],b) - 1
    return 2**ind + calc(dbl[a][ind],b)

ans = []
it = iter(ab)
for a,b in zip(it,it):
    a -= 1
    b -= 1
    a,b = min(a,b),max(a,b)
    ans.append(calc(a,b))

print('\n'.join(map(str,ans)))

# print(dbl_l)
# print(dbl_r)
# for i in range(20):




'''
ダブリングじゃー
'''
