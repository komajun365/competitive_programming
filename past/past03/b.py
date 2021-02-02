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

n,m,q = map(int,readline().split())
s = [ list(map(int,i.split())) for i in readlines()]

collect = [set() for _ in range(m+1)]
ans = []
for ss in s:
    if(ss[0]==1):
        i = ss[1]
        point = 0
        for j in range(1,m+1):
            if(i in collect[j]):
                point += n - len(collect[j])
        ans.append(point)
    else:
        collect[ss[2]].add(ss[1])

print('\n'.join(map(str,ans)))
