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
t = list(map(int,input().split()))

base = set([0,2,4,5,7,9,11])
ans = -1
for i in range(12):
    for j in t:
        if(not (j-i)%12 in base):
            break
    else:
        if(ans==-1):
            ans = i
        else:
            print(-1)
            exit()

print(ans)
