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

n,x,m = map(int,input().split())
first = [0] * (m+1)

a = [x]
first[x] = 1
for i in range(2,m+10):
    x = pow(x,2,m)
    if(first[x] != 0):
        break
    first[x] = i
    a.append(x)

# print(a)

if(i-1 >= n):
    ans = sum(a[:n])
    print(ans)
    exit()

cyc = a[first[x]-1:]
for j in range(1,len(cyc)):
    cyc[j] += cyc[j-1]

ans = sum(a[:first[x]-1])
# print(ans)
rem = n - first[x] + 1
ans += cyc[-1] * (rem//len(cyc))
# print(ans)
if(rem%len(cyc) != 0):
    ans += cyc[rem%len(cyc) - 1]
print(ans)

# print(cyc)
