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

all,n,m,*data = list(map(int,read().split()))
l = data[:n]
xy = data[n:]

ls = []
for i in range(n-1):
    ls.append(l[i+1] - l[i])
ls.sort()

xyi = []
it = iter(xy)
i = 0
for x,y in zip(it,it):
    xyi.append([x,y,i])
    i += 1

xyi.sort(key=lambda x : x[0]+x[1])

ans = [0] * m
merge = 0
ls_ind = 0
for x,y,i in xyi:
    width = x+y
    while(ls_ind < n-1):
        if(ls[ls_ind] <= width):
            merge += ls[ls_ind]
            ls_ind += 1
        else:
            break
    ans[i] = (width+1) * (n-ls_ind) + merge - max(0,x+1-l[0]) - max(0,l[-1]+y-all)

print('\n'.join(map(str,ans)))
