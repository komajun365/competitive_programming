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

if(a[0] != 0):
    print(-1)
    exit()

if(n==1):
    print(0)
    exit()

ans = a[-1]
for i in range(n-2,-1,-1):
    if(a[i+1] - a[i] == 1):
        continue
    elif(a[i+1] - a[i] > 1):
        print(-1)
        exit()
    ans += a[i]

print(ans)


'''
・Xiが0である
・Xi+1 - Xi が最大1である

なんか後ろから数えればいけるのでは？

'''
