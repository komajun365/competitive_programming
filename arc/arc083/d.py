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

n = int(readline())
a = list(map(int,read().split()))

rem = set()
ans = sum(a)//2
for i in range(n-2):
    for j in range(i+1,n-1):
        for k in range(j+1,n):
            x = [a[i*n+j], a[i*n+k], a[j*n+k]]
            max_x = max(x)
            if(max_x == x[0]):
                ind = i*n+j
            elif(max_x == x[1]):
                ind = i*n+k
            else:
                ind = j*n+k
            x.sort()
            if(x[2] > x[0]+x[1]):
                print(-1)
                exit()
            elif(x[2] == x[0]+x[1]):
                rem.add(ind)

for i in rem:
    ans -= a[i]

print(ans)
