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

n,m = map(int,readline().split())
y,x,c = map(int,readline().split())
y -= 1
x -= 1
data = list(map(int,read().split()))

black = sum(data)

if(data[y*m+x] == c):
    print(black)
    exit()

done = [0] * (n*m)
done[y*m+x] = 1
stack = [y*m+x]
while(stack):
    num = stack.pop()
    for d in [-m,m,-1,1]:
        new = num + d
        if(new<0)|(new>=n*m):
            continue
        if(num%m==0)&(d==-1):
            continue
        if(num%m==(m-1)%m)&(d==1):
            continue
        if(done[new]==1):
            continue
        if(data[new] != c):
            done[new] = 1
            stack.append(new)

cnt = sum(done)
if(c==0):
    black -= cnt
else:
    black += cnt

print(black)
