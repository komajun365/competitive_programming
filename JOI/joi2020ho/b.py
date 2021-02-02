# a,b = map(int,input().split())
# a = list(map(int,input().split()))
# a = [list(map(int,input().split())) for _ in range(n)]

# import sys
# read = sys.stdin.buffer.read
# readline = sys.stdin.buffer.readline
# readlines = sys.stdin.buffer.readlines

# 検討5分　実装11分 バグとり11分

import sys
import os
f = open('../../input.txt', 'r')
sys.stdin = f

# 二分木
import bisect

n,k = map(int,input().split())
s = input()

where = [[],[],[]]
for i,ch in enumerate(s):
    if(ch=='J'):
        where[0].append(i)
    elif(ch=='O'):
        where[1].append(i)
    else:
        where[2].append(i)

for i in range(3):
    if(len(where[i])==0):
        print(-1)
        exit()

ans = n
i_max = len(where[1])
for i in range(i_max-k+1):
    o_l = where[1][i]
    o_r = where[1][i+k-1]

    j_l = bisect.bisect_left(where[0],o_l) - k
    if(j_l < 0):
        continue

    i_r = bisect.bisect_left(where[2],o_r) + k - 1
    if(i_r >= len(where[2])):
        continue

    ans = min(ans, where[2][i_r] - where[0][j_l] + 1 - 3*k)

if(ans==n):
    ans = -1
print(ans)

print(n,k)
print(where)



'''
使うOの場所を決める
使うOで一番左側の座標をol、
使うOで一番右側の座標をorとする。

使うJで一番左側は

'''
