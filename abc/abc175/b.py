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
l = list(map(int,input().split()))
l.sort()

ans = 0
for i in range(n-2):
    li = l[i]
    for j in range(i+1,n-1):
        lj = l[j]
        for k in range(j+1,n):
            lk = l[k]
            if(li==lj)|(lj==lk):
                continue
            if(li+lj <= lk):
                continue
            ans += 1
print(ans)
