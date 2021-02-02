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
b = list(map(int, input().split()))

ans = [0] * n
for i in range(1,n+1):
    num = -1
    for j in range(n+1-i):
        if(b[j] == j+1):
            num = j
    if(num == -1):
        print(-1)
        exit()
    ans[-i] = num + 1
    del b[num]

print('\n'.join(map(str, ans)))
